# -*- coding: utf-8 -*-

from django.conf import settings
from django.template import RequestContext
from django.core.paginator import Paginator
from django.db.models.query import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from manage.forms import EntryForm, Entry_DetailForm, CategoryForm, SubCategoryForm, WriterForm, PublisherForm
from book.models import Book, BookDetail, Category, SubCategory, Writer, Publisher
from manage.dirhandler import mkdir, rmdir, movedir
from manage.view_common import *

BASE_TYPE = 'book'
TMPL_NAME = 'manage/book/book.html'
LIST_TMPL_NAME = 'manage/book/book_list.html'


@login_required
def book_add(request, set_type='entry'):
    getTitle = titleSelecter(BASE_TYPE, set_type)
    if request.method == 'POST':
        getform = {'entry': EntryForm,
                   'detail': Entry_DetailForm,
                   'category': CategoryForm,
                   'subcategory': SubCategoryForm,
                   'writer': WriterForm,
                   'publisher': PublisherForm,
                  }[request.POST['set_type']]
        set_form = getform(request.POST)
        if set_form.is_valid():
            try:
                mkdir(request.POST)
                entry_form = set_form.save()
                entry_form.save()
            except:
                return render_to_response(TMPL_NAME,
                                          {'msg': ERROR_MSG_FILEPATH,
                                           'base_type': BASE_TYPE,
                                           'set_type': set_type,
                                           'title': getTitle},
                                          context_instance=RequestContext(request))
        else:
            return render_to_response(TMPL_NAME,
                                      {'msg': ERROR_MSG_ADD,
                                       'base_type': BASE_TYPE,
                                       'set_type': set_type,
                                       'title': getTitle},
                                      context_instance=RequestContext(request))
        return render_to_response(TMPL_NAME,
                                  {'msg': MSG_ADD,
                                   'base_type': BASE_TYPE,
                                   'set_type': set_type,
                                   'title': getTitle},
                                  context_instance=RequestContext(request))
    else:
        getForm = {'entry': EntryForm(label_suffix=''),
                   'detail': Entry_DetailForm(label_suffix=''),
                   'category': CategoryForm(label_suffix=''),
                   'subcategory': SubCategoryForm(label_suffix=''),
                   'writer': WriterForm(label_suffix=''),
                   'publisher': PublisherForm(label_suffix=''),
                  }[set_type]
    return render_to_response(TMPL_NAME,
                              {'getForm': getForm,
                               'base_type': BASE_TYPE,
                               'set_type': set_type,
                               'title': getTitle},
                              context_instance=RequestContext(request))


@login_required
def book_edit_list(request, set_type):
    getModel = {'entry': Book,
                'detail': BookDetail,
                'category': Category,
                'subcategory': SubCategory,
                'writer': Writer,
                'publisher': Publisher,
              }[set_type]
    if set_type == 'entry':
        query_set = getModel.objects.all().order_by('subcategory')
    elif set_type == 'detail':
        query_set = getModel.objects.all().order_by('entry', 'volume')
    elif set_type == 'category' or set_type == 'subcategory':
        query_set = getModel.objects.all().order_by('sort_num')
    elif set_type == 'writer':
        query_set = getModel.objects.all().order_by('category')
    else:
        query_set = getModel.objects.all().order_by('name')
    getTitle = titleSelecter(BASE_TYPE, set_type)
    try:
        page_id = request.GET['page']
    except:
        page_id = 1;
    p = Paginator(query_set, settings.NUM_IN_MANAGE_LIST)
    pageData = p.page(page_id)
    return object_list(request, queryset=query_set,
                       template_name = LIST_TMPL_NAME,
                       extra_context = {'set_type': set_type,
                                        'title': getTitle,
                                        'start_index': pageData.start_index(),
                                        'end_index': pageData.end_index()
                                        },
                       paginate_by=settings.NUM_IN_MANAGE_LIST)


@login_required
def book_search(request, set_type):
    getModel = {'entry': Book,
                'detail': BookDetail,
                'category': Category,
                'subcategory': SubCategory,
                'writer': Writer,
                'publisher': Publisher,
              }[set_type]

    # タイトル取得
    getTitle = titleSelecter(BASE_TYPE, set_type)

    # キーワード取得
    if request.method == 'POST':
        keyword = request.POST['search'].encode('utf-8')
    else:
        keyword = request.GET.get('keyword', '').encode('utf-8')

    # 検索結果取得
    query_set = getModel.objects.all()
    if set_type == 'entry':
        for word in keyword.split():
            query_set = query_set.filter(Q(title__icontains=word)|
                                         Q(url_title__icontains=word)|
                                         Q(category__name__icontains=word)|
                                         Q(category__url_name__icontains=word)|
                                         Q(subcategory__name__icontains=word)|
                                         Q(subcategory__url_name__icontains=word)).order_by('category', 'subcategory')
    elif set_type == 'detail':
        for word in keyword.split():
            query_set = query_set.filter(Q(entry__title__icontains=word)|
                                         Q(entry__url_title__icontains=word)|
                                         Q(writer__name__icontains=word)|
                                         Q(publisher__name__icontains=word)|
                                         Q(description__icontains=word)).order_by('entry', 'volume')
    elif set_type == 'category':
        for word in keyword.split():
            query_set = query_set.filter(Q(name__icontains=word)|
                                         Q(url_name__icontains=word)).order_by('sort_num')
    elif set_type == 'subcategory':
        for word in keyword.split():
            query_set = query_set.filter(Q(category__name__icontains=word)|
                                         Q(category__url_name__icontains=word)|
                                         Q(name__icontains=word)|
                                         Q(url_name__icontains=word)).order_by('sort_num')
    elif set_type == 'writer':
        for word in keyword.split():
            query_set = query_set.filter(name__icontains=word).order_by('category')
    elif set_type == 'publisher':
        for word in keyword.split():
            query_set = query_set.filter(name__icontains=word)

    # ページ情報取得
    try:
        page_id = request.GET['page']
    except:
        page_id = 1;
    p = Paginator(query_set, settings.NUM_IN_MANAGE_LIST)
    pageData = p.page(page_id)

    return object_list(request,
                       queryset=query_set,
                       template_name=LIST_TMPL_NAME,
                       extra_context = {'set_type': set_type,
                                        'title': getTitle,
                                        'keyword': keyword,
                                        'start_index': pageData.start_index(),
                                        'end_index': pageData.end_index()
                                        },
                       paginate_by=settings.NUM_IN_MANAGE_LIST)


@login_required
def book_edit(request, set_type, id):
    getModel = {'entry': Book,
                'detail': BookDetail,
                'category': Category,
                'subcategory': SubCategory,
                'writer': Writer,
                'publisher': Publisher,
              }[set_type]

    getForm = {'entry': EntryForm,
               'detail': Entry_DetailForm,
               'category': CategoryForm,
               'subcategory': SubCategoryForm,
               'writer': WriterForm,
               'publisher': PublisherForm,
              }[set_type]
    getTitle = titleSelecter(BASE_TYPE, set_type)

    if request.method == 'POST':
        entry = getModel.objects.get(pk=id)
        setForm = getForm(request.POST, instance=entry)
        if setForm.is_valid():
            try:
                movedir(request.POST, id)
                entry_form = setForm.save()
                entry_form.save()
            except:
                return render_to_response(TMPL_NAME,
                                          {'msg': ERROR_MSG_FILEPATH,
                                           'title': getTitle,
                                           'base_type': BASE_TYPE,
                                           'set_type': set_type},
                                          context_instance=RequestContext(request))
        else:
            return render_to_response(TMPL_NAME,
                                      {'msg': ERROR_MSG_EDIT,
                                       'title': getTitle,
                                       'base_type': BASE_TYPE,
                                       'set_type': set_type},
                                      context_instance=RequestContext(request))
        return render_to_response(TMPL_NAME,
                                  {'msg': MSG_EDIT,
                                   'title': getTitle,
                                   'base_type': BASE_TYPE,
                                   'set_type': set_type},
                                   context_instance=RequestContext(request))
    else:
        query_set = getModel.objects.get(pk=id)
        setForm = getForm(instance=query_set, label_suffix='')
    return render_to_response(TMPL_NAME,
                              {'getForm': setForm,
                               'title': getTitle,
                               'set_type': set_type,
                               'id': id},
                              context_instance=RequestContext(request))


@login_required
def book_delete(request, set_type, id):
    getmodel = {'entry': Book,
                'detail': BookDetail,
                'category': Category,
                'subcategory': SubCategory,
                'writer': Writer,
                'publisher': Publisher,
               }[set_type]
    getTitle = titleSelecter(BASE_TYPE, set_type)
    if request.method == 'POST':
        rmdir(request.POST)
        query_set = getmodel.objects.get(pk=id)
        query_set.delete()
        return render_to_response(TMPL_NAME,
                                  {'msg': MSG_DELET,
                                   'base_type': BASE_TYPE,
                                   'title': getTitle,
                                   'set_type': set_type},
                                  context_instance=RequestContext(request))


@login_required
def book_delete_checked(request, set_type):
    getmodel = {'entry': Book,
                'detail': BookDetail,
                'category': Category,
                'subcategory': SubCategory,
                'writer': Writer,
                'publisher': Publisher,
               }[set_type]
    getTitle = titleSelecter(BASE_TYPE, set_type)
    dataArr = {'set_type': set_type}
    if request.method == 'POST':
        for i in request.POST.getlist('del_flag'):
            query_set = getmodel.objects.get(pk=i)
            if set_type == 'category':
                dataArr['url_name'] = query_set.url_name
            elif set_type == 'subcategory':
                dataArr['url_name'] = query_set.url_name
                dataArr['category'] = query_set.category_id
            elif set_type == 'entry':
                dataArr['category']    = query_set.category_id
                dataArr['subcategory'] = query_set.subcategory_id
                dataArr['url_title']   = query_set.url_title
            rmdir(dataArr)
            query_set.delete()
        return render_to_response(TMPL_NAME,
                                  {'msg': MSG_CHECKED_DELET,
                                   'base_type': BASE_TYPE,
                                   'title': getTitle,
                                   'set_type': set_type},
                                  context_instance=RequestContext(request))
