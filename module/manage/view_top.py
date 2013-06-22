# -*- coding: utf-8 -*-

import re

from django.db import transaction
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from module.common.pager import get_pager
from module.manage.forms import WhatNewFormSet
from module.top.api import create_whatnew, delete_whatnew_cache, edit_whatnew
from module.top.models import WhatNew


def _render(template_file, context):
    return render_to_response('manage/top/{}'.format(template_file), context)


@login_required
def whatnew_index(request):
    context = RequestContext(request, {})
    if request.session.get('msg_dict', False):
        context['msg_dict'] = request.session['msg_dict']
        del request.session['msg_dict']
    whatnew_list = WhatNew.all_list()
    page_id = request.GET.get('page', 1)
    pager, whatnew_list = get_pager(whatnew_list, page_id, settings.NUM_IN_MANAGE_LIST)
    context['whatnew_list'] = whatnew_list
    context.update(pager)
    return _render('index.html', context)


@login_required
@transaction.commit_on_success
def whatnew_regist(request):
    context = RequestContext(request, {})
    if request.method == 'POST':
        formset = WhatNewFormSet(request.POST)
        if formset.is_valid():
            create_whatnew(formset.cleaned_data)
            request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_REGIST}
            return HttpResponseRedirect(reverse('manage_top_index'))
        else:
            context['is_form_error'] = True
            context['formset'] = formset
            return _render('regist.html', context)
    else:
        context['formset'] = WhatNewFormSet()
    return _render('regist.html', context)


@login_required
def whatnew_edit(request, whatnew_id):
    context = RequestContext(request, {'id': whatnew_id})
    if request.method == 'POST':
        formset = WhatNewFormSet(request.POST)
        if formset.is_valid():
            edit_whatnew(formset.cleaned_data)
            request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_EDIT}
            return HttpResponseRedirect(reverse('manage_top_index'))
        else:
            context['is_form_error'] = True
            context['formset'] = formset
            return _render('edit.html', context)
    else:
        whatnew = WhatNew.get_cache(whatnew_id)
        context['formset'] = WhatNewFormSet(initial=[whatnew.__dict__])
    return _render('edit.html', context)


@login_required
@transaction.commit_on_success
def whatnew_delete(request, whatnew_id):
    request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_DELET}
    whatnew = WhatNew.objects.select_for_update().get(id=whatnew_id)
    whatnew.delete()
    return HttpResponseRedirect(reverse('manage_top_index'))


@login_required
@transaction.commit_on_success
def whatnew_delete_checked(request):
    if request.method == 'POST':
        request.session['msg_dict'] = {'info_type': settings.SUCCESS, 'msg': settings.MSG_CHECKED_DELET}
        whatnew_id_list = [whatnew_id for whatnew_id in request.POST.getlist('del_flag')]
        WhatNew.objects.select_for_update().filter(id__in=whatnew_id_list).delete()
        delete_whatnew_cache(whatnew_id_list)
        return HttpResponseRedirect(reverse('manage_top_index'))
    else:
        return HttpResponseRedirect(reverse('manage_top_index'))


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
