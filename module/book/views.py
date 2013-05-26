# -*- coding: utf-8 -*-

import re

from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from module.common.pager import get_pager
from module.book.models import Book, BookDetail, Category, SubCategory


def _render(template_file, context):
    return render_to_response('book/{}'.format(template_file), context)


@login_required
def index(request):
    context = RequestContext(request, {'category_list': Category.get_category_list()})
    return _render('index.html', context)


@login_required
def category(request, category_id):
    category_id = int(category_id)
    book_list = Category.get_book_list_by_category_id(category_id)
    page_id = request.GET.get('page', 1)
    pager, book_list = get_pager(book_list, page_id, settings.NUM_IN_LIST_PAGE)
    context = RequestContext(request, {
        'book_list': book_list,
        'category_list': Category.get_category_list(),
        'name': Category.get_cache(category_id).name,
    })
    context.update(pager)
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
        'category_list': Category.get_category_list(),
        'name': SubCategory.get_cache(subcategory_id).name,
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
        'book_detail_list': book_detail_list,
        'category_list': Category.get_category_list(),
    })
    context.update(pager)
    return _render('detail.html', context)


@login_required
def preview(request, book_id, volume):
    pass
    # query_set = BookDetail.objects.filter(entry__url_title__exact=title).get(volume__exact=volume)
    # return render_to_response('book/preview.html', context_instance=RequestContext(request, {'object': query_set, 'param_category': category}))


@login_required
def extend_detail(request, category_id, subcategory_id, title, volume):
    query_set = BookDetail.objects.filter(entry__url_title__exact=title).get(volume__exact=volume)
    return render_to_response('book/extend_detail.html', context_instance=RequestContext(request, {'object': query_set, 'param_category': category}))


@login_required
def search(request):
    if request.method == 'POST':
        keyword = request.POST['search']
    else:
        keyword = request.GET.get('keyword', '')

    book_list = []
    all_book_list = Book.get_all_list()
    for word in keyword.split():
        word = u'.*{}.*'.format(unicode(word))
        r = re.compile(word)
        for book in all_book_list:
            if r.search(book.title):
                book_list.append(book)

    page_id = request.GET.get('page', 1)
    pager, book_list = get_pager(book_list, page_id, settings.NUM_IN_LIST_PAGE)
    context = RequestContext(request, {
        'book_list': book_list,
        'category_list': Category.get_category_list(),
    })
    context.update(pager)
    return _render('search.html', context)
