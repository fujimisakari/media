# -*- coding: utf-8 -*-

from django.http import HttpResponse
from book.models import Book, BookDetail, SubCategory, Writer


def getSubcategoryList(request):
    # 指定したカテゴリからサブカテゴリ一覧を取得
    subcategoryList = '<option selected="selected" value="">---------</option>|'
    for row in SubCategory.objects.filter(category=request.GET['category_id']).order_by('sort_num'):
        subcategoryList += "<option value=\"%d\">%s</option>|" % (row.id, row.name)
    return HttpResponse(subcategoryList, mimetype="text/javascript")


def getWriterList(request):
    # 指定したカテゴリから著者名一覧を取得
    writerList = '<option selected="selected" value="">---------</option>|'
    for row in Writer.objects.filter(category=request.GET['category_id']):
        writerList += "<option value=\"%d\">%s</option>|" % (row.id, row.name)
    return HttpResponse(writerList, mimetype="text/javascript")


def getTitleList(request):
    # 指定したサブカテゴリからタイトル一覧を取得
    titleList = '<option selected="selected" value="">---------</option>|'
    for row in Book.objects.filter(subcategory=request.GET['subcategory_id']):
        titleList += "<option value=\"%d\">%s</option>|" % (row.id, row.title)
    return HttpResponse(titleList, mimetype="text/javascript")


def getVolumeList(request):
    # 指定したタイトルからvolume一覧を取得
    volumeList = '<option selected="selected" value="">---------</option>|'
    for row in BookDetail.objects.filter(entry=request.GET['entry_id']):
        volumeList += "<option value=\"%d\">%s</option>|" % (row.volume, row.volume)
    return HttpResponse(volumeList, mimetype="text/javascript")
