# -*- coding: utf-8 -*-

from module.book.models import Book, BookDetail, Category, SubCategory


def get_status_info():

    result_dict = {}
    category_list = Category.get_category_list()

    category_book_dict = {c.id: [] for c in category_list}
    subcategory_book_dict = {sc.id: [] for sc in SubCategory.get_cache_all()}
    category_detail_dict = {c.id: [] for c in category_list}

    for book in Book.get_cache_all():
        category_book_dict[book.category_id].append(book)
        subcategory_book_dict[book.subcategory_id].append(book)

    for book_detail in BookDetail.get_cache_all():
        if book_detail.book:
            category_detail_dict[book_detail.book.category_id].append(book_detail)

    # タイトル数
    category_title_info = {'total_title_count': len(Book.get_cache_all()), 'title_list': []}
    for c in category_list:
        tmp_dict = {'category': c}
        tmp_dict['title_count'] = len(category_book_dict[c.id])
        category_title_info['title_list'].append(tmp_dict)

    # 冊数
    category_book_info = {'total_book_count': len(BookDetail.get_cache_all()), 'book_list': []}
    for c in category_list:
        tmp_dict = {'category': c}
        tmp_dict['book_count'] = len(category_detail_dict[c.id])
        category_book_info['book_list'].append(tmp_dict)

    # カテゴリ別タイトル数
    subcategory_book_list = []
    for c in category_list:
        tmp_dict = {'category': c, 'title_list': []}
        for sc in c.get_subcategory_list():
            d = {'subcategory': sc}
            d['title_count'] = len(subcategory_book_dict[sc.id])
            tmp_dict['title_list'].append(d)
        subcategory_book_list.append(tmp_dict)

    subcategory_book_dict = {sc.id: [] for sc in SubCategory.get_cache_all()}
    for book in Book.get_cache_all():
        category_book_dict[book.category_id].append(book)

    result_dict = {
        'category_title_info': category_title_info,
        'category_book_info': category_book_info,
        'subcategory_book_list': subcategory_book_list,
    }
    return result_dict
