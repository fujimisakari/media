# -*- coding: utf-8 -*-

from django.http import HttpResponse
from module.book.models import Book, BookDetail, SubCategory, Writer, Publisher


def get_subcategory_list(request):
    # 指定したカテゴリからサブカテゴリ一覧を取得
    subcategoryList = '<option selected="selected" value="">---------</option>|'
    for row in sorted([x for x in SubCategory.get_cache_all() if x.category_id == int(request.GET['category_id'])], key=lambda x: x.sort):
        subcategoryList += "<option value=\"%d\">%s</option>|" % (row.id, row.name)
    return HttpResponse(subcategoryList, mimetype="text/javascript")


def get_writer_list(request):
    # 指定したカテゴリから著者名一覧を取得
    writerList = '<option selected="selected" value="">---------</option>|'
    none_wirter = [x for x in Writer.get_cache_all() if not x.category_id][0]
    writerList += "<option value=\"%d\">%s</option>|" % (none_wirter.id, none_wirter.name)
    for row in sorted([x for x in Writer.get_cache_all() if x.category_id == int(request.GET['category_id'])], key=lambda x: x.name):
        writerList += "<option value=\"%d\">%s</option>|" % (row.id, row.name)
    return HttpResponse(writerList, mimetype="text/javascript")


def get_publisher_list(request):
    # 指定したカテゴリから出版会社一覧を取得
    publisherList = '<option selected="selected" value="">---------</option>|'
    none_publisher = [x for x in Publisher.get_cache_all() if not x.category_id][0]
    publisherList += "<option value=\"%d\">%s</option>|" % (none_publisher.id, none_publisher.name)
    for row in sorted([x for x in Publisher.get_cache_all() if x.category_id == int(request.GET['category_id'])], key=lambda x: x.name):
        publisherList += "<option value=\"%d\">%s</option>|" % (row.id, row.name)
    return HttpResponse(publisherList, mimetype="text/javascript")


def get_title_list(request):
    # 指定したサブカテゴリからタイトル一覧を取得
    titleList = '<option selected="selected" value="">---------</option>|'
    for row in sorted([x for x in Book.get_cache_all() if int(request.GET['subcategory_id']) == x.subcategory_id], key=lambda x: x.subcategory_id):
        titleList += "<option value=\"%d\">%s</option>|" % (row.id, row.title)
    return HttpResponse(titleList, mimetype="text/javascript")


def get_volume_list(request):
    # 指定したタイトルからvolume一覧を取得
    volumeList = '<option selected="selected" value="">---------</option>|'
    for row in sorted([x for x in BookDetail.get_cache_all() if int(request.GET['book_id']) == x.book_id], key=lambda x: x.volume):
        volumeList += "<option value=\"%d\">%s</option>|" % (row.volume, row.volume)
    return HttpResponse(volumeList, mimetype="text/javascript")
