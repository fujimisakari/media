# -*- coding: utf-8 -*-

import re
import copy

from django.db import transaction
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from module.common.pager import get_pager
from module.manage.forms import BookFormSet, BookDetailFormSet, CategoryFormSet, SubCategoryFormSet, WriterFormSet, PublisherFormSet
from module.book.models import Book, BookDetail, Category, SubCategory, Writer, Publisher
from module.common.dirhandler import mkdir, rmdir, movedir


FORM_MAP = {'book': BookFormSet,
            'detail': BookDetailFormSet,
            'category': CategoryFormSet,
            'subcategory': SubCategoryFormSet,
            'writer': WriterFormSet,
            'publisher': PublisherFormSet,
            }

MODEL_MAP = {'book': Book,
             'detail': BookDetail,
             'category': Category,
             'subcategory': SubCategory,
             'writer': Writer,
             'publisher': Publisher,
             }

TITLE_MAP = {'book': u'BOOK',
             'detail': u'BOOK詳細',
             'category': u'カテゴリ',
             'subcategory': u'サブカテゴリ',
             'writer': u'著者',
             'publisher': u'出版社',
             }


def _render(template_file, context):
    return render_to_response('manage/book/{}'.format(template_file), context)


@login_required
def book_index(request, set_type):
    context = RequestContext(request, {'set_type': set_type, 'title': TITLE_MAP[set_type]})
    if request.session.get('msg_dict', False):
        context['msg_dict'] = request.session['msg_dict']
        del request.session['msg_dict']

    model = MODEL_MAP[set_type]
    if set_type == 'book':
        edit_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.subcategory_id)
    elif set_type == 'detail':
        book_detail_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.volume)
        edit_list = sorted([x for x in book_detail_list], key=lambda x: x.book_id)
    elif set_type == 'category':
        edit_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.sort)
    elif set_type == 'subcategory':
        edit_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.sort)
        edit_list = sorted([x for x in edit_list], key=lambda x: x.category_id)
    elif set_type == 'writer':
        edit_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.category_id)
    elif set_type == 'publisher':
        edit_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.category_id)

    page_id = request.GET.get('page', 1)
    pager, edit_list = get_pager(edit_list, page_id, settings.NUM_IN_MANAGE_LIST)
    context['result_list'] = edit_list
    context.update(pager)
    return _render('index.html', context)


# @login_required
# def book_add(request, set_type='book'):
#     context = RequestContext(request, {
#         'set_type': set_type,
#         'category_list': Category.get_category_list(),
#         'subcategory_list': SubCategory.get_subcategory_list(),
#     })
#     form = FORM_MAP[set_type]
#     if request.method == 'POST':
#         set_form = form(request.POST)
#         if set_form.is_valid():
#             try:
#                 mkdir(request.POST)
#                 set_form.save()
#             except:
#                 context['msg'] = settings.ERROR_MSG_FILEPATH
#             context['msg'] = settings.MSG_ADD
#         else:
#             context['msg'] = settings.ERROR_MSG_ADD
#     else:
#         context['getForm'] = INIT_FORM_MAP[set_type]
#     return _render('index.html', context)


@login_required
@transaction.commit_on_success
def book_regist(request, set_type):
    context = RequestContext(request, {'set_type': set_type, 'title': TITLE_MAP[set_type]})
    if request.method == 'POST':
        formset = FORM_MAP[set_type](request.POST)
        if formset.is_valid():
            # CREATE_MAP[set_type](formset.cleaned_data)
            request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_REGIST}
            return HttpResponseRedirect(reverse('manage_book_index', args=[set_type]))
        else:
            context['is_form_error'] = True
            context['formset'] = formset
            return _render('regist.html', context)
    else:
        context['formset'] = FORM_MAP[set_type]()
    return _render('regist.html', context)


@login_required
def book_edit(request, set_type, edit_id):
    context = RequestContext(request, {'id': edit_id})
    model = MODEL_MAP[set_type]
    form = FORM_MAP[set_type]

    if request.method == 'POST':
        obj = model.get_cache(edit_id)
        setForm = form(request.POST, instance=obj)
        if setForm.is_valid():
            try:
                # movedir(request.POST, edit_id)
                setForm.save()
                context['msg'] = settings.MSG_EDIT
            except:
                context['msg'] = settings.ERROR_MSG_FILEPATH
        else:
            context['msg'] = settings.ERROR_MSG_EDIT
    else:
        obj = model.get_cache(edit_id)
        context['getForm'] = form(instance=obj, label_suffix='')
    return _render('index.html', context)


@login_required
def book_delete(request, set_type, del_id):
    context = RequestContext(request, {'set_type': set_type})
    model = MODEL_MAP[set_type]
    if request.method == 'POST':
        rmdir(request.POST)
        obj = model.get_cache(del_id)
        obj = copy.copy(obj)
        obj.delete()
        return _render('index.html', context)


@login_required
def book_delete_checked(request, set_type):
    context = RequestContext(request, {'set_type': set_type})
    model = MODEL_MAP[set_type]

    if request.method == 'POST':
        data_dict = {'set_type': set_type}
        for del_id in request.POST.getlist('del_flag'):
            obj = model.get_cache(del_id)
            obj = copy.copy(obj)
            if set_type == 'category':
                data_dict['category'] = obj.id
            elif set_type == 'subcategory':
                data_dict['subcategory'] = obj.id
                data_dict['category'] = obj.category_id
            elif set_type == 'book':
                data_dict['category'] = obj.category_id
                data_dict['subcategory'] = obj.subcategory_id
                data_dict['book'] = obj.id
            rmdir(data_dict)
            obj.delete()
        return _render('index.html', context)


@login_required
def book_search(request, set_type):
    if request.method == 'POST':
        keyword = request.POST['keyword']
    else:
        keyword = request.GET.get('keyword', '')
    context = RequestContext(request, {'keyword': keyword, 'set_type': set_type, 'title': TITLE_MAP[set_type]})
    model = MODEL_MAP[set_type]

    # 検索結果取得
    result_list = []
    for word in keyword.split():
        word = u'.*{}.*'.format(unicode(word))
        r = re.compile(word, re.IGNORECASE)
        if set_type == 'book':
            search_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.subcategory_id)
            for book in search_list:
                if r.search(book.title) or r.search(book.category.name) or r.search(book.subcategory.name):
                    result_list.append(book)
        elif set_type == 'detail':
            book_detail_list = sorted([x for x in model.get_cache_all()], key=lambda x: x.volume)
            search_list = sorted([x for x in book_detail_list], key=lambda x: x.book_id)
            for book_detail in search_list:
                if r.search(book_detail.book.title) or r.search(book_detail.writer.name) or r.search(book_detail.publisher.name) or r.search(book_detail.description):
                    result_list.append(book_detail)
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

    page_id = request.GET.get('page', 1)
    pager, result_list = get_pager(result_list, page_id, settings.NUM_IN_MANAGE_LIST)
    context['result_list'] = result_list
    context.update(pager)
    return _render('index.html', context)
