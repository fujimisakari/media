# -*- coding: utf-8 -*-

from django.conf import settings
from book.models import Book, BookDetail, Category, SubCategory


def common_context(request):
    return {
        'MEDIA_TITLE': settings.MEDIA_TITLE,
        'MEDIA_BASE': settings.MEDIA_BASE,
        'MEDIA_URL': settings.MEDIA_URL,
        'MEDIA_DATA': settings.MEDIA_DATA,
        'MEDIA_CSS': settings.MEDIA_CSS,
        'MEDIA_JS': settings.MEDIA_JS,
        'MEDIA_FOTTER': settings.MEDIA_FOTTER,
        'LOGOUT_URL': settings.LOGOUT_URL,
        'CHANGE_PASSWD': settings.CHANGE_PASSWD,
    }


def book_context(request):
    return {
        'BOOK_BASE': settings.BOOK_BASE,
        'BOOK_DETAIL': settings.BOOK_DETAIL,
        'BOOK_SEARCH': settings.BOOK_SEARCH,
        'BOOK_PDF': settings.BOOK_PDF,
        'BOOK_IPAD': settings.BOOK_IPAD,
        'BOOK_IPHONE': settings.BOOK_IPHONE,
        'BOOK_DATA': settings.BOOK_DATA,
        'BOOK_THUMBNAIL': settings.BOOK_THUMBNAIL,
        'BOOK_VOLUME_THUMBNAIL': settings.BOOK_VOLUME_THUMBNAIL,
        'BOOK_THUMB_HEIGHT': settings.BOOK_THUMB_HEIGHT,
        'BOOK_THUMB_WIDTH': settings.BOOK_THUMB_WIDTH,
        'it_list': Book.objects.filter(category__url_name='it').order_by('title').select_related()[:settings.ALL_LIST_LIMIT],
        'managa_list': Book.objects.filter(category__url_name='manga').order_by('title').select_related()[:settings.ALL_LIST_LIMIT],
        'recent_book_list': BookDetail.objects.order_by('-create_date')[:settings.LIST_COUNT],
        'category_list': Category.objects.all().order_by('sort_num'),
        'subcategory_list': SubCategory.objects.all().order_by('sort_num'),
        'entry_list': Book.objects.all().order_by('title')
    }


def movie_context(request):
    return {
        'MOVIE_BASE': settings.MOVIE_BASE,
    }


def music_context(request):
    return {
        'MUSIC_BASE': settings.MUSIC_BASE,
    }


def manage_context(request):
    return {
        'MANAGE_BASE': settings.MANAGE_BASE,
        'MANAGE_TOP': settings.MANAGE_TOP,
        'MANAGE_BOOK': settings.MANAGE_BOOK,
        'MANAGE_MOVIE': settings.MANAGE_MOVIE,
        'MANAGE_MUSIC': settings.MANAGE_MUSIC,
        'MANAGE_UPLOAD': settings.MANAGE_UPLOAD,
        'MANAGE_ANALYSIS': settings.MANAGE_ANALYSIS,
    }


def image_context(request):
    return {
        'RECENT_BOOK': settings.RECENT_BOOK,
        'RECENT_MOVIE': settings.RECENT_MOVIE,
        'RECENT_MUSIC': settings.RECENT_MUSIC,
        'HEADER_TITLE': settings.HEADER_TITLE,
        'HEADER_TOP1': settings.HEADER_TOP1,
        'HEADER_BOOK1': settings.HEADER_BOOK1,
        'HEADER_MOVIE1': settings.HEADER_MOVIE1,
        'HEADER_MUSIC1': settings.HEADER_MUSIC1,
        'HEADER_MANAGE1': settings.HEADER_MANAGE1,
        'HEADER_UPLOAD': settings.HEADER_UPLOAD,
        'HEADER_TOP2': settings.HEADER_TOP2,
        'HEADER_BOOK2': settings.HEADER_BOOK2,
        'HEADER_MOVIE2': settings.HEADER_MOVIE2,
        'HEADER_MUSIC2': settings.HEADER_MUSIC2,
        'HEADER_MANAGE2': settings.HEADER_MANAGE2,
        'NAVI_MANAGE': settings.NAVI_MANAGE,
        'NAVI_CATEAGORY': settings.NAVI_CATEAGORY,
        'NAVI_SUBCATEGORY': settings.NAVI_SUBCATEGORY,
        'NAVI_SEARCH': settings.NAVI_SEARCH,
        'MAIN_WHATNEW': settings.MAIN_WHATNEW,
        'MAIN_INFO': settings.MAIN_INFO,
        'MAIN_ALL_LIST': settings.MAIN_ALL_LIST,
        'MAIN_CATEGORY': settings.MAIN_CATEGORY,
        'MAIN_SUBCATEGORY': settings.MAIN_SUBCATEGORY,
        'MAIN_SEARCH': settings.MAIN_SEARCH,
        'MAIN_DETAIL': settings.MAIN_DETAIL,
        'MAIN_PREVIEW': settings.MAIN_PREVIEW,
        'MAIN_BACK': settings.MAIN_BACK,
        'LOGIN_TITLE': settings.LOGIN_TITLE,
        'CHPW_TITLE': settings.CHPW_TITLE,
    }
