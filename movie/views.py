# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms

def top(request):
    return render_to_response('movie/top.html', {}, context_instance=RequestContext(request))
