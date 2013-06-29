# -*- coding: utf-8 -*-

import re

from django.db import transaction
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from module.common.pager import get_pager
from module.manage.forms import BookFormSet, BookDetailFormSet, CategoryFormSet, SubCategoryFormSet, WriterFormSet, PublisherFormSet, WhatNewFormSet
from module.book.models import Book, BookDetail, SubCategory, Writer, Publisher
from module.manage.api import MODEL_MAP, regist_data, delete_data, edit_data, get_status_info


FORM_MAP = {'whatnew': WhatNewFormSet,
            'book': BookFormSet,
            'detail': BookDetailFormSet,
            'category': CategoryFormSet,
            'subcategory': SubCategoryFormSet,
            'writer': WriterFormSet,
            'publisher': PublisherFormSet,
            }


def _render(template_file, context):
    return render_to_response('manage/{}'.format(template_file), context)


@login_required
def index(request, set_type='whatnew'):
    context = RequestContext(request, {'set_type': set_type, 'title': settings.TITLE_MAP[set_type]})
    if request.session.get('msg_dict', False):
        context['msg_dict'] = request.session['msg_dict']
        del request.session['msg_dict']

    model = MODEL_MAP[set_type]
    if set_type == 'whatnew':
        result_list = model.all_list()
    elif set_type == 'book':
        result_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.subcategory_id)
    elif set_type == 'detail':
        book_detail_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.volume)
        result_list = sorted([x for x in book_detail_list], key=lambda x: x.book_id)
    elif set_type == 'category':
        result_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.sort)
    elif set_type == 'subcategory':
        result_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.sort)
        result_list = sorted([x for x in result_list], key=lambda x: x.category_id)
    elif set_type == 'writer':
        result_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.category_id)
    elif set_type == 'publisher':
        result_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.category_id)

    page_id = request.GET.get('page', 1)
    pager, result_list = get_pager(result_list, page_id, settings.NUM_IN_MANAGE_LIST)
    context['result_list'] = result_list
    context.update(pager)
    return _render('index.html', context)


@login_required
@transaction.commit_on_success
def regist(request, set_type):
    context = RequestContext(request, {'set_type': set_type, 'title': settings.TITLE_MAP[set_type]})
    if request.method == 'POST':
        formset = FORM_MAP[set_type](request.POST)
        if formset.is_valid() and formset.cleaned_data[0]:
            regist_data(set_type, formset.cleaned_data[0])
            request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_REGIST}
            return HttpResponseRedirect(reverse('manage_index', args=[set_type]))
        else:
            context['is_form_error'] = True
            context['formset'] = formset
            return _render('regist.html', context)
    else:
        context['formset'] = FORM_MAP[set_type]()
    return _render('regist.html', context)


@login_required
def edit(request, set_type, edit_id):
    context = RequestContext(request, {
        'id': edit_id,
        'set_type': set_type,
        'title': settings.TITLE_MAP[set_type],
        'subcategory_list': SubCategory.get_subcategory_list(),
        'writer_list': Writer.get_cache_all(),
        'publisher_list': Publisher.get_cache_all(),
    })
    if set_type == 'detail':
        context['book_list'] = Book.get_all_list()
        context['detail'] = BookDetail.get_cache(edit_id)
    model = MODEL_MAP[set_type]

    if request.method == 'POST':
        formset = FORM_MAP[set_type](request.POST)
        if formset.is_valid() and formset.cleaned_data[0]:
            edit_data(set_type, formset.cleaned_data[0])
            request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_EDIT}
            return HttpResponseRedirect(reverse('manage_index', args=[set_type]))
        else:
            context['is_form_error'] = True
            context['formset'] = formset
            return _render('edit.html', context)
    else:
        obj = model.get_cache(edit_id)
        context['formset'] = FORM_MAP[set_type](initial=[obj.__dict__])
    return _render('edit.html', context)


@login_required
@transaction.commit_on_success
def delete(request, set_type, del_id):
    request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_DELET}
    delete_data(set_type, [del_id])
    return HttpResponseRedirect(reverse('manage_index', args=[set_type]))


@login_required
@transaction.commit_on_success
def delete_checked(request, set_type):
    if request.method == 'POST':
        obj_id_list = [obj_id for obj_id in request.POST.getlist('del_flag')]
        if obj_id_list:
            delete_data(set_type, obj_id_list)
            request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_CHECKED_DELET}
        return HttpResponseRedirect(reverse('manage_index', args=[set_type]))
    else:
        return HttpResponseRedirect(reverse('manage_index', args=[set_type]))


@login_required
def search(request, set_type):
    if request.method == 'POST':
        keyword = request.POST['keyword']
    else:
        keyword = request.GET.get('keyword', '')
    context = RequestContext(request, {'keyword': keyword, 'set_type': set_type, 'title': settings.TITLE_MAP[set_type]})
    model = MODEL_MAP[set_type]

    # 検索結果取得
    result_list = []
    for word in keyword.split():
        word = u'.*{}.*'.format(unicode(word))
        r = re.compile(word, re.IGNORECASE)
        if set_type == 'whatnew':
            search_list = model.get_cache_all()
            for whatnew in search_list:
                if r.search(whatnew.content):
                    result_list.append(whatnew)
        elif set_type == 'book':
            search_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.subcategory_id)
            for book in search_list:
                if r.search(book.title) or r.search(book.category.name) or r.search(book.subcategory.name):
                    result_list.append(book)
        elif set_type == 'detail':
            search_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.book_id)
            for book_detail in search_list:
                if r.search(book_detail.book.title) or r.search(book_detail.description):
                    result_list.append(book_detail)
            result_list = sorted([x for x in result_list], key=lambda x: x.volume)
        elif set_type == 'category':
            search_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.sort)
            for category in search_list:
                if r.search(category.name):
                    result_list.append(book)
        elif set_type == 'subcategory':
            search_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.sort)
            for subcategory in search_list:
                if r.search(subcategory.name) or r.search(subcategory.category.name):
                    result_list.append(subcategory)
        elif set_type == 'writer':
            search_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.category_id)
            for writer in search_list:
                if r.search(writer.name):
                    result_list.append(subcategory)
        elif set_type == 'publisher':
            search_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.category_id)
            for publisher in search_list:
                if r.search(publisher.name):
                    result_list.append(publisher)
    result_list = list(set(result_list))

    page_id = request.GET.get('page', 1)
    pager, result_list = get_pager(result_list, page_id, settings.NUM_IN_MANAGE_LIST)
    context['result_list'] = result_list
    context.update(pager)
    return _render('index.html', context)


@login_required
def status(request):
    context = RequestContext(request, {'status_info': get_status_info()})
    return _render('status.html', context)


# import os.path
# from django.conf import settings
# from django.template import RequestContext
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render_to_response
# from django import forms
# from module.book.models import Category, SubCategory, Book, BookDetail
# from module.manage.view_common import *


# class UploadEntryForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ('category_id', 'subcategory_id')


# class UploadFileForm(forms.ModelForm):
#     upload_file = forms.FileField()

#     class Meta:
#         model = BookDetail
#         fields = ('book_id', 'volume')


# def create_path(post_data):
#     volume = forms.IntegerField()
#     category = Category.objects.get(pk=post_data['category'])
#     subcategory = SubCategory.objects.get(pk=post_data['subcategory'])
#     entry = Book.objects.get(pk=post_data['entry'])
#     get_data_type = {'thumbnail': '_thumbnail.jpg',
#                      'pdf': '_pc.pdf',
#                      'epud': '_ipad.epud',
#                      'zip': '_data.zip',
#                      }[post_data['data_type']]
#     filename = "%s%s" % (post_data['volume'], get_data_type)

#     path = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, subcategory.url_name, entry.url_title, filename)
#     return path


# @login_required
# def uploader(request, set_type='book'):
#     getTitle = titleSelecter('upload', set_type)
#     tmplName = 'manage/upload/book.html'

#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 path = create_path(request.POST)
#                 create_file = open(path, mode='w')
#                 upfile = request.FILES['upload_file']
#                 for chunk in upfile.chunks():
#                     create_file.write(chunk)
#                 create_file.close()
#             except:
#                 return render_to_response(tmplName,
#                                           {'msg': ERROR_MSG_FILEPATH,
#                                            'base_type': 'upload',
#                                            'title': getTitle},
#                                           context_instance=RequestContext(request))
#         else:
#             return render_to_response(tmplName,
#                                       {'msg': ERROR_MSG_UPLOAD,
#                                        'base_type': 'upload',
#                                        'title': getTitle},
#                                       context_instance=RequestContext(request))
#         return render_to_response(tmplName,
#                                   {'msg': MSG_UPLOAD,
#                                    'base_type': 'upload',
#                                    'title': getTitle},
#                                   context_instance=RequestContext(request))
#     else:
#         form_entry = UploadEntryForm(label_suffix='')
#         form_upload = UploadFileForm(label_suffix='')
#     return render_to_response(tmplName,
#                               {'form_entry': form_entry,
#                                'form_upload': form_upload,
#                                'title': getTitle},
#                               context_instance=RequestContext(request))
