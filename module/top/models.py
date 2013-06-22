# -*- coding: utf-8 -*-

from django.db import models
from module.common.abustractmodel import AbustractCachedModel


class WhatNew(AbustractCachedModel):
    create_date = models.DateTimeField(u'作成日', auto_now_add=True)
    content = models.TextField(u'内容', blank=True)

    @classmethod
    def all_list(cls):
        return sorted([whatnew for whatnew in cls.get_cache_all()], key=lambda x: x.id, reverse=True)
