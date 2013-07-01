# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.core.cache import cache
from module.book.models import Book, BookDetail, Category, SubCategory, Writer, Publisher
from module.top.models import WhatNew


MODEL_MAP = {'whatnew': WhatNew,
             'book': Book,
             'detail': BookDetail,
             'category': Category,
             'subcategory': SubCategory,
             'writer': Writer,
             'publisher': Publisher,
             }


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


def regist_data(set_type, data):
    model = MODEL_MAP[set_type]

    if set_type == 'whatnew':
        model.objects.create(
            create_date=data['create_date'],
            content=data['content'],
        )
    elif set_type == 'book':
        book = model.objects.create(
            title=data['title'],
            category_id=data['category_id'],
            subcategory_id=data['subcategory_id'],
            writer_id=data['writer_id'],
            publisher_id=data['publisher_id'],
        )
        book_path = '{}{}/{}/{}'.format(settings.BOOK_DATA_PATH, book.category_id, book.subcategory_id, book.id)
        img_path = '{}{}/{}/{}'.format(settings.THUMBNAIL_DATA_PATH, book.category_id, book.subcategory_id, book.id)
        os.mkdir(book_path)
        os.mkdir(img_path)
    elif set_type == 'detail':
        # 空の場合はデフォルト値を入れる
        if not data['volume']:
            data['volume'] = 1
        model.objects.create(
            book_id=data['book_id'],
            volume=data['volume'],
            pdf_size=data['pdf_size'],
            total_page=data['total_page'],
            exit_attachment=data['exit_attachment'],
            description=data['description'],
        )
    elif set_type == 'category':
        category = model.objects.create(
            name=data['name'],
            sort=data['sort'],
        )
        book_path = '{}{}'.format(settings.BOOK_DATA_PATH, category.id)
        img_path = '{}{}'.format(settings.THUMBNAIL_DATA_PATH, category.id)
        os.mkdir(book_path)
        os.mkdir(img_path)
    elif set_type == 'subcategory':
        subcategory = model.objects.create(
            category_id=data['category_id'],
            name=data['name'],
            sort=data['sort'],
        )
        book_path = '{}{}/{}'.format(settings.BOOK_DATA_PATH, subcategory.category_id, subcategory.id)
        img_path = '{}{}/{}'.format(settings.THUMBNAIL_DATA_PATH, subcategory.category_id, subcategory.id)
        os.mkdir(book_path)
        os.mkdir(img_path)
    elif set_type == 'writer':
        model.objects.create(
            category_id=data['category_id'],
            name=data['name'],
        )
    elif set_type == 'publisher':
        model.objects.create(
            category_id=data['category_id'],
            name=data['name'],
        )


def edit_data(set_type, data):
    model = MODEL_MAP[set_type]

    if set_type == 'whatnew':
        model.objects.select_for_update().update(
            id=data['id'],
            create_date=data['create_date'],
            content=data['content'],
        )
    elif set_type == 'book':
        book = model.objects.select_for_update().get(id=data['id'])
        before_book_path = '{}{}/{}/{}'.format(settings.BOOK_DATA_PATH, book.category_id, book.subcategory_id, book.id)
        before_img_path = '{}{}/{}/{}'.format(settings.THUMBNAIL_DATA_PATH, book.category_id, book.subcategory_id, book.id)
        book.title = data['title']
        book.category_id = data['category_id']
        book.subcategory_id = data['subcategory_id']
        book.writer_id = data['writer_id']
        book.publisher_id = data['publisher_id']
        after_book_path = '{}{}/{}/{}'.format(settings.BOOK_DATA_PATH, book.category_id, book.subcategory_id, book.id)
        after_img_path = '{}{}/{}/{}'.format(settings.THUMBNAIL_DATA_PATH, book.category_id, book.subcategory_id, book.id)
        if before_book_path != after_book_path:
            os.rename(before_book_path, after_book_path)
            os.rename(before_img_path, after_img_path)
        book.save()
    elif set_type == 'detail':
        model.objects.select_for_update().update(
            id=data['id'],
            book_id=data['book_id'],
            volume=data['volume'],
            pdf_size=data['pdf_size'],
            total_page=data['total_page'],
            exit_attachment=data['exit_attachment'],
            description=data['description'],
        )
    elif set_type == 'category':
        model.objects.select_for_update().update(
            id=data['id'],
            name=data['name'],
            sort=data['sort'],
        )
    elif set_type == 'subcategory':
        subcategory = model.objects.select_for_update().get(id=data['id'])
        before_book_path = '{}{}/{}'.format(settings.BOOK_DATA_PATH, subcategory.category_id, subcategory.id)
        before_img_path = '{}{}/{}'.format(settings.THUMBNAIL_DATA_PATH, subcategory.category_id, subcategory.id)
        subcategory.category_id = data['category_id']
        subcategory.name = data['name']
        subcategory.sort = data['sort']
        after_book_path = '{}{}/{}'.format(settings.BOOK_DATA_PATH, subcategory.category_id, subcategory.id)
        after_img_path = '{}{}/{}'.format(settings.THUMBNAIL_DATA_PATH, subcategory.category_id, subcategory.id)
        if before_book_path != after_book_path:
            os.rename(before_book_path, after_book_path)
            os.rename(before_img_path, after_img_path)
        subcategory.save()
    elif set_type == 'writer':
        model.objects.select_for_update().update(
            id=data['id'],
            category_id=data['category_id'],
            name=data['name'],
        )
    elif set_type == 'publisher':
        model.objects.select_for_update().update(
            id=data['id'],
            category_id=data['category_id'],
            name=data['name'],
        )
    cache.delete(model.get_cache_path(data['id']))
    cache.delete(model.get_cache_all_path())


def delete_data(set_type, del_id_list):
    model = MODEL_MAP[set_type]

    for del_id in del_id_list:
        obj = model.objects.select_for_update().get(id=del_id)
        if set_type == 'book':
            before_book_path = '{}{}/{}/{}'.format(settings.BOOK_DATA_PATH, obj.category_id, obj.subcategory_id, obj.id)
            after_book_path = '{}{}/{}/del_{}'.format(settings.BOOK_DATA_PATH, obj.category_id, obj.subcategory_id, obj.id)
            before_img_path = '{}{}/{}/{}'.format(settings.THUMBNAIL_DATA_PATH, obj.category_id, obj.subcategory_id, obj.id)
            after_img_path = '{}{}/{}/del_{}'.format(settings.THUMBNAIL_DATA_PATH, obj.category_id, obj.subcategory_id, obj.id)
            os.rename(before_book_path, after_book_path)
            os.rename(before_img_path, after_img_path)
            BookDetail.objects.filter(book_id=obj.id).delete()
        elif set_type == 'category':
            before_book_path = '{}{}'.format(settings.BOOK_DATA_PATH, obj.id)
            after_book_path = '{}del_{}'.format(settings.BOOK_DATA_PATH, obj.id)
            before_img_path = '{}{}'.format(settings.THUMBNAIL_DATA_PATH, obj.id)
            after_img_path = '{}del_{}'.format(settings.THUMBNAIL_DATA_PATH, obj.id)
            os.rename(before_book_path, after_book_path)
            os.rename(before_img_path, after_img_path)
        elif set_type == 'subcategory':
            before_book_path = '{}{}/{}'.format(settings.BOOK_DATA_PATH, obj.category_id, obj.id)
            after_book_path = '{}{}/del_{}'.format(settings.BOOK_DATA_PATH, obj.category_id, obj.id)
            before_img_path = '{}{}/{}'.format(settings.THUMBNAIL_DATA_PATH, obj.category_id, obj.id)
            after_img_path = '{}{}/del_{}'.format(settings.THUMBNAIL_DATA_PATH, obj.category_id, obj.id)
            os.rename(before_book_path, after_book_path)
            os.rename(before_img_path, after_img_path)
            book_list = Book.objects.filter(subcategory_id=obj.id)
            for book in book_list:
                BookDetail.objects.filter(book_id=book.id).delete()
                book.delete()
        obj.delete()
        cache.delete(model.get_cache_path(del_id))
    cache.delete(model.get_cache_all_path())


def upload_data(data, upload_file):

    if not data['volume']:
        data['volume'] = 1

    if int(data['upload_type']) == 1:
        file_path = '{}{}/{}/{}/{}{}'.format(settings.THUMBNAIL_DATA_PATH, data['category_id'], data['subcategory_id'],
                                             data['book_id'], data['volume'], settings.BOOK_VOLUME_THUMBNAIL)
    elif int(data['upload_type']) == 2:
        file_path = '{}{}/{}/{}/{}{}'.format(settings.BOOK_DATA_PATH, data['category_id'], data['subcategory_id'],
                                             data['book_id'], data['volume'], settings.BOOK_PDF)
    create_file = open(file_path, mode='w')
    for chunk in upload_file.chunks():
        create_file.write(chunk)
    create_file.close()
