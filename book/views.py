# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import connection
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from django.db.models.query import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator

from book.models import Entry, Entry_Detail, Category, SubCategory
from book.hyperestraier import search_index


@login_required
def all_list(request):
    sql = '''
SELECT
    be.title,
    be.url_title,
    be.cid,
    be.c_url_name,
    be.sc_url_name,
    to_char(update_date, 'yyyy-mm-dd') as date
FROM
    book_entry_detail as bed
LEFT JOIN
    (SELECT
         sbe.id as e_id,
         sbe.category_id,
         sbe.title,
         sbe.url_title,
         sbc.id as cid,
         sbc.url_name as c_url_name,
         sbs.url_name as sc_url_name
     FROM
         book_entry as sbe
     LEFT JOIN
         book_category as sbc
     ON
         sbe.category_id = sbc.id
     LEFT JOIN
         book_subcategory as sbs
     ON
         sbe.subcategory_id = sbs.id
     ) as be
on
    bed.entry_id = be.e_id
group by
    1, 2, 3, 4, 5, 6
ORDER BY
    date desc
'''
    cursor = connection.cursor()
    cursor.execute(sql)
    item_arr = []
    category_arr = []
    roop_num1 = 1
    for row1 in cursor.fetchall():
        tmp_arr = {}
        tmp_arr['title'] = row1[0]
        tmp_arr['url'] = row1[1]
        tmp_arr['cid'] = row1[2]
        tmp_arr['curl'] = row1[3]
        tmp_arr['scurl'] = row1[4]
        if roop_num1 == 1:
            item_arr.append(tmp_arr)
            category_arr.append(row1[2])
        else:
            isImport = 1
            for row2 in item_arr:
                if row1[1] == row2['url']:
                    isImport = 0
                    break
            if isImport == 1:
                item_arr.append(tmp_arr)
                category_arr.append(row1[2])
        roop_num1 += 1
    fomat_category_arr = list(set(category_arr))

    new_item_arr = []
    limit = settings.ALL_LIST_LIMIT
    for cid in fomat_category_arr:
        loop_num2 = 1
        for item_row in item_arr:
            if limit >= loop_num2:
                if cid == item_row['cid']:
                    tmp_arr = {}
                    tmp_arr['title'] = item_row['title']
                    tmp_arr['url'] = item_row['url']
                    tmp_arr['cid'] = item_row['cid']
                    tmp_arr['curl'] = item_row['curl']
                    tmp_arr['scurl'] = item_row['scurl']
                    new_item_arr.append(tmp_arr)
                    loop_num2 += 1
            else:
                roop_num2 = 1
                break
    return render_to_response('book/all_list.html', context_instance=RequestContext(request, {'aobject': new_item_arr, 'limit_num': settings.ALL_LIST_LIMIT}))


@login_required
def category(request, category):
    query_set = Entry.objects.filter(category__url_name=category).order_by('subcategory')
    category_query = Category.objects.get(url_name=category)
    category_name  = category_query.name
    try:
        page_id = request.GET['page']
    except:
        page_id = 1
    p = Paginator(query_set, settings.NUM_IN_LIST_PAGE)
    pageData = p.page(page_id)
    return object_list(request, queryset=query_set, paginate_by=settings.NUM_IN_LIST_PAGE,
                       template_name='book/category.html', extra_context=dict(param_category=category,
                                                                              category_name=category_name,
                                                                              start_index=pageData.start_index(),
                                                                              end_index=pageData.end_index()
                                                                              ))


@login_required
def subcategory(request, category, subcategory):
    query_set = Entry.objects.filter(subcategory__url_name=subcategory).order_by('title')
    subcategory_query = SubCategory.objects.get(url_name=subcategory)
    subcategory_name  = subcategory_query.name
    try:
        page_id = request.GET['page']
    except:
        page_id = 1
    p = Paginator(query_set, settings.NUM_IN_LIST_PAGE)
    pageData = p.page(page_id)
    return object_list(request, queryset=query_set, paginate_by=settings.NUM_IN_LIST_PAGE,
                       template_name='book/subcategory.html', extra_context=dict(param_category=category,
                                                                                 param_subcategory=subcategory,
                                                                                 subcategory_name=subcategory_name,
                                                                                 start_index=pageData.start_index(),
                                                                                 end_index=pageData.end_index()
                                                                                 ))


@login_required
def detail(request, category, subcategory, title):
    query_set = Entry_Detail.objects.filter(entry__url_title__exact=title).order_by('volume').select_related()
    try:
        page_id = request.GET['page']
    except:
        page_id = 1
    p = Paginator(query_set, settings.NUM_IN_DETAIL_PAGE)
    pageData = p.page(page_id)
    return object_list(request, queryset=query_set, paginate_by=settings.NUM_IN_DETAIL_PAGE,
                       template_name='book/detail.html', extra_context=dict(param_category=category,
                                                                            start_index=pageData.start_index(),
                                                                            end_index=pageData.end_index()
                                                                            ))


@login_required
def preview(request, category, subcategory, title, volume):
    query_set = Entry_Detail.objects.filter(entry__url_title__exact=title).get(volume__exact=volume)
    return render_to_response('book/preview.html', context_instance=RequestContext(request, {'object': query_set, 'param_category': category}))


@login_required
def extend_detail(request, category, subcategory, title, volume):
    query_set = Entry_Detail.objects.filter(entry__url_title__exact=title).get(volume__exact=volume)
    return render_to_response('book/extend_detail.html', context_instance=RequestContext(request, {'object': query_set, 'param_category': category}))


@login_required
def search(request):
    if request.method == 'POST':
        keyword = request.POST['search'].encode('utf-8')
    else:
        keyword = request.GET.get('keyword', '').encode('utf-8')
    query_set = Entry.objects.all()
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
