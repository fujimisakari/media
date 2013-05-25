# -*- coding: utf-8 -*-

from django.db import models
from common.abustractmodel import AbustractCachedModel


class Category(AbustractCachedModel):
    name = models.CharField(u'カテゴリ名', max_length=100, unique=True)
    url_name = models.CharField(u'URL名', max_length=100, unique=True)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)


class SubCategory(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID')
    name = models.CharField(u'サブカテゴリ名', max_length=100, unique=True)
    url_name = models.CharField(u'URL名', max_length=100, unique=True)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)


class Book(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID')
    subcategory_id = models.IntegerField(u'サブカテゴリID')
    title = models.CharField(u'タイトル名', max_length=100, unique=True)
    url_name = models.CharField(u'URL名', max_length=100, unique=True)


class BookDetail(AbustractCachedModel):
    book_id = models.IntegerField(u'ブックID')
    volume = models.IntegerField(u'巻')
    pdf_size = models.IntegerField(u'PDFサイズ')
    epud_size = models.IntegerField(u'EPUDサイズ')
    total_page = models.IntegerField(u'ページ数')
    writer_id = models.IntegerField(u'著者', null=True)
    publisher_id = models.IntegerField(u'出版社', null=True)
    description = models.TextField(u'備考', null=True, blank=True)
    exit_pdf = models.BooleanField(u'PDF有無', default=False)
    exit_epud = models.BooleanField(u'EPUD有無', default=False)
    exit_attachment = models.BooleanField(u'付属CD-R有無', default=False)
    update_date = models.DateTimeField(u'更新日', auto_now=True)
    create_date = models.DateTimeField(u'作成日', auto_now_add=True)

    @property
    def book(self):
        return Book.get_cache(self.book_id)

    @classmethod
    def get_recent_book_list(cls, limit=3):
        book_detail_list = sorted([book_detail for book_detail in cls.get_cache_all()], key=lambda x: x.id, reverse=True)
        return book_detail_list[:limit]


class Writer(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID', null=True, blank=True)
    name = models.CharField(u'著者', max_length=100, unique=True)


class Publisher(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID', null=True, blank=True)
    name = models.CharField(u'出版社', max_length=100, unique=True)
