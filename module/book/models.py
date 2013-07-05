# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from module.common.abustractmodel import AbustractCachedModel


class Category(AbustractCachedModel):
    name = models.CharField(u'カテゴリ名', max_length=100, unique=True)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)

    @property
    def title_count(self):
        return len([book for book in Book.get_cache_all() if self.id == book.category_id])

    @property
    def book_count(self):
        return len([book_detail for book_detail in BookDetail.get_cache_all() if book_detail.book and self.id == book_detail.book.category_id])

    @classmethod
    def get_category_list(cls):
        return sorted([category for category in cls.get_cache_all()], key=lambda x: x.sort)

    def get_subcategory_list(self):
        return sorted([subcategory for subcategory in SubCategory.get_cache_all() if self.id == subcategory.category_id], key=lambda x: x.sort)

    def get_book_list(self):
        book_detail_list = sorted([book_detail for book_detail in BookDetail.get_cache_all()], key=lambda x: x.update_date, reverse=True)
        book_list = []
        for book_detail in book_detail_list:
            if not book_detail.book in book_list:
                book_list.append(book_detail.book)
        return [book for book in book_list if book and book.category_id == self.id][:settings.ALL_LIST_LIMIT]

    @classmethod
    def get_book_list_by_category_id(cls, category_id):
        book_detail_list = sorted([book_detail for book_detail in BookDetail.get_cache_all()], key=lambda x: x.update_date, reverse=True)
        book_list = []
        for book_detail in book_detail_list:
            if not book_detail.book in book_list:
                book_list.append(book_detail.book)
        return [book for book in book_list if book and book.category_id == category_id]


class SubCategory(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID')
    name = models.CharField(u'サブカテゴリ名', max_length=100)
    sort = models.IntegerField(u'Sort番号', blank=True, null=True)

    class Meta:
        unique_together = (('category_id', 'name'),)

    @property
    def category(self):
        return Category.get_cache(self.category_id)

    @property
    def title_count(self):
        return len([book for book in Book.get_cache_all() if self.id == book.subcategory_id])

    @classmethod
    def get_subcategory_list(cls):
        return sorted([subcategory for subcategory in cls.get_cache_all()], key=lambda x: x.sort)

    def get_book_list(self):
        book_detail_list = [book_detail for book_detail in BookDetail.get_cache_all() if book_detail.book and book_detail.book.category_id == self.category_id]
        book_detail_list = [book_detail for book_detail in book_detail_list if book_detail.book.subcategory_id == self.id]
        book_detail_list = list(sorted(book_detail_list, key=lambda x: x.update_date, reverse=True))

        book_list = []
        for book_detail in book_detail_list:
            if not book_detail.book in book_list:
                book_list.append(book_detail.book)
        return book_list


class Book(AbustractCachedModel):
    category_id = models.IntegerField(u'カテゴリID', db_index=True)
    subcategory_id = models.IntegerField(u'サブカテゴリID', db_index=True)
    title = models.CharField(u'タイトル名', max_length=100)
    writer_id = models.IntegerField(u'著者', null=True)
    publisher_id = models.IntegerField(u'出版社', null=True)
    thumbnail_volume = models.IntegerField(u'サムネイルで表示するvolume', default=1)

    @property
    def img_path(self):
        return u'/img/thumbnail/{}/{}/{}/{}{}'.format(self.category_id, self.subcategory_id, self.id, self.thumbnail_volume, settings.BOOK_VOLUME_THUMBNAIL)

    @property
    def category(self):
        return Category.get_cache(self.category_id)

    @property
    def subcategory(self):
        return SubCategory.get_cache(self.subcategory_id)

    @classmethod
    def get_all_list(cls):
        return sorted([book for book in cls.get_cache_all()], key=lambda x: x.subcategory_id)

    @property
    def writer(self):
        return Writer.get_cache(self.writer_id)

    @property
    def publisher(self):
        return Publisher.get_cache(self.publisher_id)

    @property
    def detail_list(self):
        return sorted([book_detail for book_detail in BookDetail.get_cache_all() if book_detail.book_id == self.id], key=lambda x: x.volume)


class BookDetail(AbustractCachedModel):
    book_id = models.IntegerField(u'ブックID', db_index=True)
    volume = models.IntegerField(u'巻', default=1)
    pdf_size = models.IntegerField(u'PDFサイズ', default=0)
    epud_size = models.IntegerField(u'EPUDサイズ', default=0)
    total_page = models.IntegerField(u'ページ数', default=0)
    description = models.TextField(u'備考', blank=True)
    exit_pdf = models.BooleanField(u'PDF有無', default=True)
    exit_epud = models.BooleanField(u'EPUD有無', default=False)
    exit_attachment = models.BooleanField(u'付属CD-R有無', default=False)
    update_date = models.DateTimeField(u'更新日', auto_now=True)
    create_date = models.DateTimeField(u'作成日', auto_now_add=True)

    class Meta:
        unique_together = (('book_id', 'volume'),)

    @property
    def book(self):
        return Book.get_cache(self.book_id)

    @property
    def img_path(self):
        return u'/img/thumbnail/{}/{}/{}/{}{}'.format(self.book.category_id, self.book.subcategory_id, self.book_id, self.volume, settings.BOOK_VOLUME_THUMBNAIL)

    @property
    def download_path(self):
        return u'/book/download/{}/{}/{}/{}/'.format(self.book.category_id, self.book.subcategory_id, self.book_id, self.volume)

    @classmethod
    def get_book_detail_list_by_book_id(cls, book_id):
        return sorted([book_detail for book_detail in cls.get_cache_all() if book_detail.book_id == book_id], key=lambda x: x.volume)

    @classmethod
    def get_recent_book_list(cls, limit=3):
        book_detail_list = sorted([book_detail for book_detail in cls.get_cache_all()], key=lambda x: x.update_date, reverse=True)
        book_list = []
        for book_detail in book_detail_list:
            if not book_detail.book in book_list:
                book_list.append(book_detail.book)
        return [book for book in book_list if book][:limit]

    @property
    def volume_range(self):
        volume_range_list = []
        extra_volume = 0
        for row in sorted([x for x in self.get_cache_all() if self.book_id == x.book_id], key=lambda x: x.volume):
            volume_range_list.append(row.volume)
            extra_volume = row.volume + 1
        volume_range_list.append(extra_volume)
        return volume_range_list


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
