# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from module.common.abustractmodel import AbustractCachedModel


class Category(AbustractCachedModel):
    name = models.CharField(u'カテゴリ名', max_length=100, unique=True)
    url_name = models.CharField(u'URL名', max_length=100, unique=True)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)

    @property
    def title_count(self):
        return len([book for book in Book.get_cache_all() if self.id == book.category_id])

    @property
    def book_count(self):
        return len([book_detail for book_detail in BookDetail.get_cache_all() if self.id == book_detail.book.category_id])

    @classmethod
    def get_category_list(cls):
        return sorted([category for category in cls.get_cache_all()], key=lambda x: x.sort)

    def get_subcategory_list(self):
        return sorted([subcategory for subcategory in SubCategory.get_cache_all() if self.id == subcategory.category_id], key=lambda x: x.sort)

    def get_book_list(self):
        book_detail_list = sorted([book_detail for book_detail in BookDetail.get_cache_all()], key=lambda x: x.update_date, reverse=True)
        book_list = list(set([book_detail.book for book_detail in book_detail_list]))
        return [book for book in book_list if book.category_id == self.id][:settings.ALL_LIST_LIMIT]

    @classmethod
    def get_book_list_by_category_id(cls, category_id):
        book_detail_list = sorted([book_detail for book_detail in BookDetail.get_cache_all()], key=lambda x: x.update_date, reverse=True)
        book_list = list(set([book_detail.book for book_detail in book_detail_list]))
        return [book for book in book_list if book.category_id == category_id]


class SubCategory(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID')
    name = models.CharField(u'サブカテゴリ名', max_length=100, unique=True)
    url_name = models.CharField(u'URL名', max_length=100, unique=True)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)

    @property
    def category(self):
        return Category.get_cache(self.category_id)

    @property
    def title_count(self):
        return len([book for book in Book.get_cache_all() if self.id == book.subcategory_id])


class Book(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID')
    subcategory_id = models.IntegerField(u'サブカテゴリID')
    title = models.CharField(u'タイトル名', max_length=100, unique=True)
    url_name = models.CharField(u'URL名', max_length=100, unique=True)

    @property
    def category(self):
        return Category.get_cache(self.category_id)

    @property
    def subcategory(self):
        return SubCategory.get_cache(self.subcategory_id)

    @classmethod
    def get_all_list(cls):
        return sorted([book for book in cls.get_cache_all()], key=lambda x: x.subcategory_id)


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

    @property
    def writer(self):
        return Writer.get_cache(self.writer_id)

    @property
    def publisher(self):
        return Publisher.get_cache(self.publisher_id)

    @classmethod
    def get_book_detail_list_by_book_id(cls, book_id):
        return sorted([book_detail for book_detail in cls.get_cache_all() if book_detail.book_id == book_id], key=lambda x: x.volume)

    @classmethod
    def get_recent_book_list(cls, limit=3):
        book_detail_list = sorted([book_detail for book_detail in cls.get_cache_all()], key=lambda x: x.update_date, reverse=True)
        return book_detail_list[:limit]


class Writer(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID', null=True, blank=True)
    name = models.CharField(u'著者', max_length=100, unique=True)

    @property
    def category(self):
        return Category.get_cache(self.category_id)


class Publisher(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID', null=True, blank=True)
    name = models.CharField(u'出版社', max_length=100, unique=True)

    @property
    def category(self):
        return Category.get_cache(self.category_id)
