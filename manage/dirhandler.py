# -*- coding: utf-8 -*-

import os
import shutil
from book.models import Entry, Category, SubCategory
from django.conf import settings


def mkdir(post_data):
    if post_data['set_type'] == 'category':
        path = os.path.join(settings.MANAGE_BOOK_PATH, post_data['url_name'])
        os.mkdir(path)

    if post_data['set_type'] == 'subcategory':
        category = Category.objects.get(pk=post_data['category'])
        path = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, post_data['url_name'])
        os.mkdir(path)

    if post_data['set_type'] == 'entry':
        category = Category.objects.get(pk=post_data['category'])
        subcategory = SubCategory.objects.get(pk=post_data['subcategory'])
        path = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, subcategory.url_name, post_data['url_title'])
        os.mkdir(path)


def rmdir(post_data):
    if post_data['set_type'] == 'category':
        path = os.path.join(settings.MANAGE_BOOK_PATH, post_data['url_name'])
        shutil.rmtree(path)

    if post_data['set_type'] == 'subcategory':
        category = Category.objects.get(pk=post_data['category'])
        path = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, post_data['url_name'])
        shutil.rmtree(path)

    if post_data['set_type'] == 'entry':
        category = Category.objects.get(pk=post_data['category'])
        subcategory = SubCategory.objects.get(pk=post_data['subcategory'])
        path = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, subcategory.url_name, post_data['url_title'])
        shutil.rmtree(path)


def movedir(post_data, modele_id):
    if post_data['set_type'] == 'category':
        category = Category.objects.get(pk=modele_id)
        old_name = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name)
        new_name = os.path.join(settings.MANAGE_BOOK_PATH, post_data['url_name'])
        os.rename(old_name, new_name)

    if post_data['set_type'] == 'subcategory':
        category = Category.objects.get(pk=post_data['category'])
        subcategory = SubCategory.objects.get(pk=modele_id)
        old_name = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, subcategory.url_name )
        new_name = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, post_data['url_name'])
        os.rename(old_name, new_name)

    if post_data['set_type'] == 'entry':
        category = Category.objects.get(pk=post_data['category'])
        subcategory = SubCategory.objects.get(pk=post_data['subcategory'])
        entry = Entry.objects.get(pk=modele_id)
        old_name = os.path.join(settings.MANAGE_BOOK_PATH, entry.category.url_name, entry.subcategory.url_name, entry.url_title )
        new_name = os.path.join(settings.MANAGE_BOOK_PATH, category.url_name, subcategory.url_name, post_data['url_title'])
        os.rename(old_name, new_name)
