# -*- coding: utf-8 -*-

import re

from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from module.common.pager import get_pager
from module.book.api import get_book_list, get_subcategory_list
from module.book.models import Book, BookDetail, Category, SubCategory


def _render(template_file, context):
    return render_to_response('book/{}'.format(template_file), context)


@login_required
def index(request):
    context = RequestContext(request, {
        'result_list': get_book_list(),
    })
    return _render('index.html', context)


@login_required
def category(request, category_id):
    category_id = int(category_id)
    context = RequestContext(request, {
        'result_list': get_subcategory_list(category_id),
        'category': Category.get_cache(category_id),
    })
    return _render('category.html', context)


@login_required
def subcategory(request, category_id, subcategory_id):
    category_id, subcategory_id = int(category_id), int(subcategory_id)
    book_list = Category.get_book_list_by_category_id(category_id)
    book_list = [book for book in book_list if book.subcategory_id == subcategory_id]
    page_id = request.GET.get('page', 1)
    pager, book_list = get_pager(book_list, page_id, settings.NUM_IN_LIST_PAGE)
    context = RequestContext(request, {
        'book_list': book_list,
        'subcategory': SubCategory.get_cache(subcategory_id),
    })
    context.update(pager)
    return _render('subcategory.html', context)


@login_required
def detail(request, book_id):
    book_id = int(book_id)
    book_detail_list = BookDetail.get_book_detail_list_by_book_id(book_id)
    page_id = request.GET.get('page', 1)
    pager, book_detail_list = get_pager(book_detail_list, page_id, settings.NUM_IN_DETAIL_PAGE)
    context = RequestContext(request, {
        'book': Book.get_cache(book_id),
        'book_detail_list': book_detail_list,
    })
    context.update(pager)
    return _render('detail.html', context)


@login_required
def search(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
    else:
        keyword = request.GET.get('keyword', '')

    book_list = []
    all_book_list = sorted([x for x in Book.get_all_list()], key=lambda x: x.subcategory_id)
    for word in keyword.split():
        word = u'.*{}.*'.format(unicode(word))
        r = re.compile(word, re.IGNORECASE)
        for book in all_book_list:
            if r.search(book.title) or r.search(book.category.name) or r.search(book.subcategory.name):
                book_list.append(book)
    book_list = list(set(book_list))

    page_id = request.GET.get('page', 1)
    pager, book_list = get_pager(book_list, page_id, settings.NUM_IN_LIST_PAGE)
    context = RequestContext(request, {
        'book_list': book_list,
        'keyword': keyword,
        'navi_search': True,
    })
    context.update(pager)
    return _render('search.html', context)
