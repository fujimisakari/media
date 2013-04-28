# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from book.models import Entry, Entry_Detail, Category, SubCategory, Writer, Publisher

# 指定したカテゴリからサブカテゴリ一覧を取得
def getSubcategoryList(request):
    subcategoryList = '<option selected="selected" value="">---------</option>|'
    for row in SubCategory.objects.filter(category=request.GET['category_id']).order_by('sort_num'):
        subcategoryList += "<option value=\"%d\">%s</option>|" % (row.id, row.name)
    return  HttpResponse(subcategoryList, mimetype="text/javascript")

# 指定したカテゴリから著者名一覧を取得
def getWriterList(request):
    writerList = '<option selected="selected" value="">---------</option>|'
    for row in Writer.objects.filter(category=request.GET['category_id']):
        writerList += "<option value=\"%d\">%s</option>|" % (row.id, row.name)
    return  HttpResponse(writerList, mimetype="text/javascript")

# 指定したサブカテゴリからタイトル一覧を取得
def getTitleList(request):
    titleList = '<option selected="selected" value="">---------</option>|'
    for row in Entry.objects.filter(subcategory=request.GET['subcategory_id']):
        titleList += "<option value=\"%d\">%s</option>|" % (row.id, row.title)
    return  HttpResponse(titleList, mimetype="text/javascript")

# 指定したタイトルからvolume一覧を取得
def getVolumeList(request):
    volumeList = '<option selected="selected" value="">---------</option>|'
    for row in Entry_Detail.objects.filter(entry=request.GET['entry_id']):
        volumeList += "<option value=\"%d\">%s</option>|" % (row.volume, row.volume)
    return  HttpResponse(volumeList, mimetype="text/javascript")
