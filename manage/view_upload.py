# -*- coding: utf-8 -*-

import os.path
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django import forms
from book.models import Category, SubCategory, Entry, Entry_Detail
from manage.view_common import *


class UploadEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('category', 'subcategory')

class UploadFileForm(forms.ModelForm):
    upload_file = forms.FileField()
    class Meta:
        model = Entry_Detail
        fields = ('entry', 'volume')

def create_path(post_data):
    volume = forms.IntegerField()
    category = Category.objects.get(pk=post_data['category'])
    subcategory = SubCategory.objects.get(pk=post_data['subcategory'])
    entry = Entry.objects.get(pk=post_data['entry'])
    get_data_type = {'thumbnail': '_thumbnail.jpg',
                     'pdf': '_pc.pdf',
                     'epud': '_ipad.epud',
                     'zip': '_data.zip',
                     }[post_data['data_type']]
    filename = "%s%s" % (post_data['volume'], get_data_type)

    path = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, subcategory.url_name, entry.url_title, filename)

    return path

@login_required
def uploader(request, set_type='book'):
    getTitle = titleSelecter('upload', set_type)
    tmplName = 'manage/upload/book.html'

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                path = create_path(request.POST)
                create_file = open(path, mode='w')
                upfile = request.FILES['upload_file']
                for chunk in upfile.chunks():
                   create_file.write(chunk)
                create_file.close()
            except:
                return render_to_response(tmplName,
                                          {'msg': ERROR_MSG_FILEPATH,
                                           'base_type': 'upload',
                                           'title': getTitle},
                                          context_instance=RequestContext(request))
        else:
            return render_to_response(tmplName,
                                      {'msg': ERROR_MSG_UPLOAD,
                                       'base_type': 'upload',
                                       'title': getTitle},
                                      context_instance=RequestContext(request))
        return render_to_response(tmplName,
                                  {'msg': MSG_UPLOAD,
                                   'base_type': 'upload',
                                   'title': getTitle},
                                  context_instance=RequestContext(request))
    else:
        form_entry = UploadEntryForm(label_suffix='')
        form_upload = UploadFileForm(label_suffix='')
    return render_to_response(tmplName,
                              {'form_entry': form_entry,
                               'form_upload': form_upload,
                               'title': getTitle},
                              context_instance=RequestContext(request))
