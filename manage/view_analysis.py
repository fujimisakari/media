# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from book.models import Book, BookDetail, Category, SubCategory
from manage.view_common import *

BASE_TYPE = 'analysis'


@login_required
def analysis(request, set_type):

    tmpl_name = {'book': 'manage/analysis/book.html',
                 'movie': 'manage/analysis/movie.html',
                 'music': 'manage/analysis/music.html',
                }[set_type]
    getTitle = titleSelecter(BASE_TYPE, set_type)

    if set_type == 'book':
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

        return render_to_response(tmpl_name,
                                  {'bookArr': bookArr,
                                   'titleArr': titleArr,
                                   'subcategoryArr': subcategoryArr,
                                   'title': getTitle},
                                  context_instance=RequestContext(request))
