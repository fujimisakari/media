# -*- coding: utf-8 -*-

import copy
import re

from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from module.common.pager import get_pager
from module.manage.forms import WhatNewForm
from module.top.models import WhatNew


def _render(template_file, context):
    return render_to_response('manage/top/{}'.format(template_file), context)


@login_required
def whatnew_index(request):
    context = RequestContext(request, {'title': settings.TOP_WHATNEW})
    whatnew_list = WhatNew.all_list()
    page_id = request.GET.get('page', 1)
    pager, whatnew_list = get_pager(whatnew_list, page_id, settings.NUM_IN_MANAGE_LIST)
    context['whatnew_list'] = whatnew_list
    context.update(pager)
    return _render('index.html', context)


@login_required
def whatnew_add(request):
    context = RequestContext(request, {'title': settings.TOP_WHATNEW})
    if request.method == 'POST':
        set_form = WhatNewForm(request.POST, label_suffix='')
        if set_form.is_valid():
            set_form.save()
            context['msg'] = settings.MSG_ADD
        else:
            context['msg'] = settings.ERROR_MSG_ADD
    else:
        context['getForm'] = WhatNewForm(label_suffix='')
    return _render('regist.html', context)


@login_required
def whatnew_regist(request):
    context = RequestContext(request, {'title': settings.TOP_WHATNEW})
    if request.method == 'POST':
        set_form = WhatNewForm(request.POST, label_suffix='')
        if set_form.is_valid():
            set_form.save()
            context['msg'] = settings.MSG_ADD
        else:
            context['msg'] = settings.ERROR_MSG_ADD
    else:
        context['getForm'] = WhatNewForm(label_suffix='')
    return _render('regist.html', context)


@login_required
def whatnew_list(request):
    context = RequestContext(request, {'title': settings.TOP_WHATNEW})
    whatnew_list = WhatNew.all_list()
    page_id = request.GET.get('page', 1)
    pager, whatnew_list = get_pager(whatnew_list, page_id, settings.NUM_IN_MANAGE_LIST)
    context['whatnew_list'] = whatnew_list
    context.update(pager)
    return _render('list.html', context)


@login_required
def whatnew_edit(request, whatnew_id):
    context = RequestContext(request, {'title': settings.TOP_WHATNEW, 'id': whatnew_id})
    if request.method == 'POST':
        whatnew = WhatNew.get_cache(whatnew_id)
        whatnew = copy.copy(whatnew)
        set_form = WhatNewForm(request.POST, instance=whatnew, label_suffix='')
        if set_form.is_valid():
            set_form.save()
            context['msg'] = settings.MSG_EDIT
        else:
            context['msg'] = settings.ERROR_EDIT_ADD
    else:
        whatnew = WhatNew.get_cache(whatnew_id)
        context['getForm'] = WhatNewForm(instance=whatnew, label_suffix='')
    return _render('index.html', context)


@login_required
def whatnew_delete(request, whatnew_id):
    if request.method == 'POST':
        context = RequestContext(request, {'title': settings.TOP_WHATNEW, 'msg': settings.MSG_DELET})
        whatnew = WhatNew.get_cache(whatnew_id)
        whatnew = copy.copy(whatnew)
        whatnew.delete()
        return _render('index.html', context)


@login_required
def whatnew_delete_checked(request):
    if request.method == 'POST':
        context = RequestContext(request, {'title': settings.TOP_WHATNEW, 'msg': settings.MSG_CHECKED_DELET})
        for whatnew_id in request.POST.getlist('del_flag'):
            whatnew = WhatNew.get_cache(whatnew_id)
            whatnew = copy.copy(whatnew)
            whatnew.delete()
        return _render('index.html', context)


@login_required
def whatnew_search(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
    else:
        keyword = request.GET.get('keyword', '')
    context = RequestContext(request, {'keyword': keyword})

    whatnew_list = []
    all_whatnew_list = WhatNew.all_list()
    for word in keyword.split():
        word = u'.*{}.*'.format(unicode(word))
        r = re.compile(word, re.IGNORECASE)
        for whatnew in all_whatnew_list:
            if r.search(whatnew.content):
                whatnew_list.append(whatnew)

    page_id = request.GET.get('page', 1)
    pager, whatnew_list = get_pager(whatnew_list, page_id, settings.NUM_IN_LIST_PAGE)
    context['whatnew_list'] = whatnew_list
    context.update(pager)
    return _render('index.html', context)
