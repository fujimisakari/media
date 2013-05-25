# -*- coding: utf-8 -*-

from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from django.db.models.query import Q
from django.core.paginator import Paginator

from module.common.pager import get_pager
from module.book.models import Book, BookDetail, Category, SubCategory
# from book.hyperestraier import search_index


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
def preview(request, category_id, subcategory_id, title, volume):
    query_set = BookDetail.objects.filter(entry__url_title__exact=title).get(volume__exact=volume)
    return render_to_response('book/preview.html', context_instance=RequestContext(request, {'object': query_set, 'param_category': category}))


@login_required
def extend_detail(request, category_id, subcategory_id, title, volume):
    query_set = BookDetail.objects.filter(entry__url_title__exact=title).get(volume__exact=volume)
    return render_to_response('book/extend_detail.html', context_instance=RequestContext(request, {'object': query_set, 'param_category': category}))


@login_required
def search(request):
    if request.method == 'POST':
        keyword = request.POST['search'].encode('utf-8')
    else:
        keyword = request.GET.get('keyword', '').encode('utf-8')
    query_set = Book.objects.all()
    for word in keyword.split():
        query_set = query_set.filter(Q(title__icontains=word) | Q(url_title__icontains=word)).order_by('title')
    try:
        page_id = request.GET['page']
    except:
        page_id = 1
    p = Paginator(query_set, settings.NUM_IN_LIST_PAGE)
    pageData = p.page(page_id)
    return object_list(request, queryset=query_set, paginate_by=settings.NUM_IN_LIST_PAGE,
                       template_name='book/search.html', extra_context=dict(keyword=keyword,
                                                                            start_index=pageData.start_index(),
                                                                            end_index=pageData.end_index()
                                                                            ))

# @login_required
# def search(request):

#     if request.method == 'POST':
#         keyword = request.POST['search'].encode('utf-8')
#     else:
#         keyword = request.GET.get('keyword', '').encode('utf-8')

#     result_list = search_index(keyword)
#     paginator = Paginator(result_list, 10)

#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1

#     try:
#         contacts = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         contacts = paginator.page(paginator.num_pages)

#     return render_to_response('book/search.html',context_instance=RequestContext(request, {'contacts': contacts, 'param_keyword': keyword}))
