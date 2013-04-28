# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list
from book.models import Book, BookDetail, Category, SubCategory
from top.models import WhatNew


@login_required
def whatnew_list(request):

    bookArr = {}
    titleArr = {}
    subcategoryArr = {}

    # 総冊数
    bookArr['total_book'] = BookDetail.objects.all().count()
    # 総タイトル数
    titleArr['total_title'] = Book.objects.all().count()

    for i in Category.objects.all().order_by('sort_num'):
        # カテゴリ別総冊数
        bookArr[i.url_name] = BookDetail.objects.filter(entry__category=i.id).count()
        # カテゴリ別タイトル数
        titleArr[i.url_name] = Book.objects.filter(category=i.id).count()
        # サブカテゴリ別タイトル数
        tmpArr = []
        for sub in SubCategory.objects.filter(category=i.id).order_by('sort_num'):
            tmpDic = {}
            tmpDic[sub.url_name] = Book.objects.filter(category=i.id).filter(subcategory=sub.id).count()
            tmpArr.append(tmpDic)
        subcategoryArr[i.url_name] = tmpArr

    query_set = WhatNew.objects.all().order_by('-regist_date')
    return object_list(request,
                      queryset=query_set,
                      paginate_by=settings.NUM_IN_WHATNEW_LIST,
                      extra_context=dict(bookArr=bookArr,
                                         titleArr=titleArr,
                                         subcategoryArr=subcategoryArr))
