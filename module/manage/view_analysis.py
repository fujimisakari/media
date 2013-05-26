# -*- coding: utf-8 -*-

from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from module.book.models import Book, BookDetail, Category


def _render(template_file, context):
    return render_to_response('manage/analysis/{}'.format(template_file), context)


@login_required
def analysis(request):

    context = RequestContext(request, {
        'title': settings.ANALYSIS_BOOK,
        'total_title_count': len(Book.get_cache_all()),
        'total_book_count': len(BookDetail.get_cache_all()),
        'category_list': Category.get_category_list(),
    })

    return _render('index.html', context)
