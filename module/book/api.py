# -*- coding: utf-8 -*-

from django.conf import settings
from module.book.models import Category, BookDetail


def get_book_list():
    result_list = []
    category_list = Category.get_category_list()
    category_dict = {c.id: [] for c in category_list}
    for book_detail in BookDetail.get_cache_all():
        if book_detail.book:
            category_dict[book_detail.book.category_id].append(book_detail)

    for c in category_list:
        tmp_dict = {'category': c}
        book_detail_list = list(sorted(category_dict[c.id], key=lambda x: x.update_date, reverse=True))

        book_list = []
        for book_detail in book_detail_list:
            if not book_detail.book in book_list:
                book_list.append(book_detail.book)
        tmp_dict['book_list'] = book_list[:settings.ALL_LIST_LIMIT]
        result_list.append(tmp_dict)
    return result_list


def get_subcategory_list(category_id):
    result_list = []
    subcategory_list = Category.get_cache(category_id).get_subcategory_list()
    subcategory_dict = {sc.id: [] for sc in subcategory_list}
    for book_detail in BookDetail.get_cache_all():
        if book_detail.book and book_detail.book.category_id == category_id:
            subcategory_dict[book_detail.book.subcategory_id].append(book_detail)

    for sc in subcategory_list:
        tmp_dict = {'subcategory': sc}
        book_detail_list = list(sorted(subcategory_dict[sc.id], key=lambda x: x.update_date, reverse=True))

        book_list = []
        for book_detail in book_detail_list:
            if not book_detail.book in book_list:
                book_list.append(book_detail.book)
        tmp_dict['book_list'] = book_list
        result_list.append(tmp_dict)
    return result_list
