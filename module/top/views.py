# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from module.book.models import BookDetail
from module.top.models import WhatNew


def _render(template_file, context):
    return render_to_response('top/{}'.format(template_file), context)


@login_required
def index(request):

    context = RequestContext(request, {
        'recent_book_list': BookDetail.get_recent_book_list(limit=12),
        'whatnew_list': WhatNew.all_list(),
    })

    return _render('index.html', context)
