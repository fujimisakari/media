# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import permalink


class Category(models.Model):
    name = models.CharField(u'カテゴリ名 ※', max_length=100, unique=True, db_index=True)
    url_name = models.CharField(u'URL名 ※', max_length=100, unique=True, db_index=True)
    sort_num = models.IntegerField(u'Sort番号', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('category', (), { 'category': self.url_name })


class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'カテゴリ ※')
    name = models.CharField(u'サブカテゴリ名 ※', max_length=100, unique=True, db_index=True)
    url_name = models.CharField(u'URL名 ※', max_length=100, unique=True, db_index=True)
    sort_num = models.IntegerField(u'Sort番号', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self) :
        return ('subcategory', (), {'category': self.category.url_name, 'subcategory': self.url_name})


class Entry(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'カテゴリ ※')
    subcategory = models.ForeignKey(SubCategory, verbose_name=u'サブカテゴリ ※')
    title = models.CharField(u'タイトル名 ※', max_length=100, unique=True, db_index=True)
    url_title = models.CharField(u'URL名 ※', max_length=100, unique=True, db_index=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('detail', (), {'category': self.category.url_name, 'subcategory': self.subcategory.url_name, 'title': self.url_title})


class Writer(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'カテゴリ ※')
    name = models.CharField(u'著者 ※', max_length=100, unique=True, db_index=True)

    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(u'出版社 ※', max_length=100, unique=True, db_index=True)

    def __unicode__(self):
        return self.name


class Entry_Detail(models.Model):
    entry = models.ForeignKey(Entry, verbose_name=u'タイトル ※')
    volume = models.IntegerField(u'巻 ※')
    pdf_size = models.IntegerField(u'PDFサイズ ※')
    epud_size = models.IntegerField(u'EPUDサイズ ※')
    total_page = models.IntegerField(u'ページ数 ※')
    writer = models.ForeignKey(Writer, verbose_name=u'著者 ※', null=True)
    publisher = models.ForeignKey(Publisher, verbose_name=u'出版社 ※', null=True)
    description = models.TextField(u'備考', null=True, blank=True)
    create_date = models.DateTimeField(u'作成日', editable=False, auto_now_add=True)
    update_date = models.DateTimeField(u'更新日', editable=False, auto_now=True)
    exit_pdf = models.BooleanField(u'PDF有無', default=False)
    exit_epud = models.BooleanField(u'EPUD有無', default=False)
    exit_attachment = models.BooleanField(u'付属CD-R有無', default=False)

    def __unicode__(self):
        return self.entry.title

    @permalink
    def get_absolute_url(self):
        return ('detail', (), {'category': self.entry.category.url_name, 'subcategory': self.entry.subcategory.url_name, 'title': self.entry.url_title})
