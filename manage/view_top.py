# -*- coding: utf-8 -*-

import os.path
from django.conf import settings
from django.template import RequestContext
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from django import forms
from manage.forms import WhatNewForm
from top.models import WhatNew
from manage.view_common import *

# 定数
BASE_TYPE = 'top'
TMPL_NAME = 'manage/top/top.html'
LIST_TMPL_NAME = 'manage/top/top_list.html'

@login_required
def top_add(request, set_type='whatnew'):
    getTitle = titleSelecter(BASE_TYPE, set_type)
    if request.method == 'POST':
        set_form = WhatNewForm(request.POST, label_suffix='')
        if set_form.is_valid():
            entry_form = set_form.save()
            entry_form.save()
            return render_to_response(TMPL_NAME,
                                      {'msg': MSG_ADD,
                                       'set_type': set_type,
                                       'base_type': BASE_TYPE,
                                       'title': getTitle},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response(TMPL_NAME,
                                      {'msg': ERROR_MSG_ADD,
                                       'set_type': set_type,
                                       'base_type': BASE_TYPE,
                                       'title': getTitle},
                                      context_instance=RequestContext(request))
    else:
        getForm = WhatNewForm(label_suffix='')
    return render_to_response(TMPL_NAME,
                              {'getForm': getForm,
                               'set_type': set_type,
                               'title': getTitle},
                              context_instance=RequestContext(request))

@login_required
def top_edit_list(request, set_type):
    getTitle = titleSelecter(BASE_TYPE, set_type)
    query_set = WhatNew.objects.all().order_by('-regist_date')
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
                                        'start_index': pageData.start_index(),
                                        'end_index': pageData.end_index()
                                        },
                       paginate_by=settings.NUM_IN_MANAGE_LIST)

@login_required
def top_edit(request, set_type, id):
    getTitle = titleSelecter(BASE_TYPE, set_type)
    if request.method == 'POST':
        query_set = WhatNew.objects.get(pk=id)
        set_form = WhatNewForm(request.POST, instance=query_set, label_suffix='')
        if set_form.is_valid():
            entry_form = set_form.save()
            entry_form.save()
            return render_to_response(TMPL_NAME,
                                      {'msg': MSG_EDIT,
                                       'set_type': set_type,
                                       'base_type': BASE_TYPE,
                                       'title': getTitle},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response(TMPL_NAME,
                                      {'msg': ERROR_EDIT_ADD,
                                       'set_type': set_type,
                                       'base_type': BASE_TYPE,
                                       'title': getTitle},
                                      context_instance=RequestContext(request))
    else:
        query_set = WhatNew.objects.get(pk=id)
        getForm = WhatNewForm(instance=query_set, label_suffix='')
    return render_to_response(TMPL_NAME,
                              {'getForm': getForm,
                               'set_type': set_type,
                               'id': id,
                               'title': getTitle},
                              context_instance=RequestContext(request))

@login_required
def top_delete(request, set_type, id):
    if request.method == 'POST':
        getTitle = titleSelecter(BASE_TYPE, set_type)
        query_set = WhatNew.objects.get(pk=id)
        query_set.delete()
        return render_to_response(TMPL_NAME,
                                  {'msg': MSG_DELET,
                                   'set_type': set_type,
                                   'base_type': BASE_TYPE,
                                   'title': getTitle},
                                  context_instance=RequestContext(request))

@login_required
def top_delete_checked(request, set_type):
    if request.method == 'POST':
        getTitle = titleSelecter(BASE_TYPE, set_type)
        for i in request.POST.getlist('del_flag'):
            query_set = WhatNew.objects.get(pk=i)
            query_set.delete()
        return render_to_response(TMPL_NAME,
                                  {'msg': MSG_CHECKED_DELET,
                                   'set_type': set_type,
                                   'base_type': BASE_TYPE,
                                   'title': getTitle},
                                  context_instance=RequestContext(request))

@login_required
def top_search(request, set_type):
    getTitle = titleSelecter(BASE_TYPE, set_type)
    if request.method == 'POST':
        keyword = request.POST['search'].encode('utf-8')
    else:
        keyword = request.GET.get('keyword', '').encode('utf-8')
    query_set = WhatNew.objects.all()
    for word in keyword.split():
        query_set = query_set.filter(content__icontains=word).order_by('-regist_date')
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


