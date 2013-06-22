# -*- coding: utf-8 -*-

from django.conf import settings
from module.book.models import Category


def common_context(request):
    return {
        'MEDIA_TITLE': settings.MEDIA_TITLE,
        'MEDIA_URL': '/static',
        'MEDIA_CSS': settings.MEDIA_CSS,
        'MEDIA_JS': settings.MEDIA_JS,
        'MEDIA_FOTTER': settings.MEDIA_FOTTER,
        'category_list': Category.get_category_list(),
        'SUCCESS': settings.SUCCESS,
        'ERROR': settings.ERROR,
        'ATTENTION': settings.ATTENTION,
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
