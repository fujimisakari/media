# -*- encoding:utf-8 -*-

from django.db import models

class WhatNew(models.Model):
    regist_date = models.DateTimeField(u'登録日', editable=False, auto_now_add=True)
    content  = models.TextField(u'内容 ※', blank=True)

    def __unicode__(self):
        return self.content
