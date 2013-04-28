# -*- coding: utf-8 -*-

from django.db import models


class Category(models.Model):
    name = models.CharField(u'カテゴリ名', max_length=100, unique=True)
    url = models.CharField(u'URL', max_length=100, unique=True)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)


class SubCategory(models.Model):
    category_id = models.IntegerField(u'カテゴリID')
    name = models.CharField(u'サブカテゴリ名', max_length=100, unique=True)
    url = models.CharField(u'URL', max_length=100, unique=True)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)


class Book(models.Model):
    category_id = models.IntegerField(u'カテゴリID')
    subcategory_id = models.IntegerField(u'サブカテゴリID')
    title = models.CharField(u'タイトル名', max_length=100, unique=True)
    url = models.CharField(u'URL', max_length=100, unique=True)


class BookDetail(models.Model):
    book_id = models.IntegerField(u'ブックID')
    volume = models.IntegerField(u'巻')
    pdf_size = models.IntegerField(u'PDFサイズ')
    epud_size = models.IntegerField(u'EPUDサイズ')
    total_page = models.IntegerField(u'ページ数')
    writer_id = models.IntegerField(u'著者 ※', null=True)
    publisher_id = models.IntegerField(u'出版社 ※', null=True)
    description = models.TextField(u'備考', null=True, blank=True)
    exit_pdf = models.BooleanField(u'PDF有無', default=False)
    exit_epud = models.BooleanField(u'EPUD有無', default=False)
    exit_attachment = models.BooleanField(u'付属CD-R有無', default=False)
    update_date = models.DateTimeField(u'更新日', auto_now=True)
    create_date = models.DateTimeField(u'作成日', auto_now_add=True)


class Writer(models.Model):
    category_id = models.IntegerField(u'カテゴリID')
    name = models.CharField(u'著者', max_length=100, unique=True)


class Publisher(models.Model):
    category_id = models.IntegerField(u'カテゴリID')
    name = models.CharField(u'出版社', max_length=100, unique=True)
