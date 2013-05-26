# -*- coding: utf-8 -*-

from django.conf import settings


def common_context(request):
    return {
        'MEDIA_TITLE': settings.MEDIA_TITLE,
        'MEDIA_URL': '/static/',
        'MEDIA_CSS': settings.MEDIA_CSS,
        'MEDIA_JS': settings.MEDIA_JS,
        'MEDIA_FOTTER': settings.MEDIA_FOTTER,
    }


def book_context(request):
    return {
        'BOOK_PDF': settings.BOOK_PDF,
        'BOOK_IPAD': settings.BOOK_IPAD,
        'BOOK_IPHONE': settings.BOOK_IPHONE,
        'BOOK_DATA': settings.BOOK_DATA,
        'BOOK_THUMBNAIL': settings.BOOK_THUMBNAIL,
        'BOOK_VOLUME_THUMBNAIL': settings.BOOK_VOLUME_THUMBNAIL,
        'BOOK_THUMB_HEIGHT': settings.BOOK_THUMB_HEIGHT,
        'BOOK_THUMB_WIDTH': settings.BOOK_THUMB_WIDTH,
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
