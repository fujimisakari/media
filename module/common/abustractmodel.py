# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache


class AbustractCachedModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(AbustractCachedModel, self).save()
        cache.delete(self.get_cache_path(self.id))
        cache.delete(self.get_cache_all_path())

    def delete(self, *args, **kwargs):
        cache.delete(self.get_cache_path(self.id))
        cache.delete(self.get_cache_all_path())
        super(AbustractCachedModel, self).delete()

    @classmethod
    def get_cache_path(cls, pk):
        # classmethodはclassからもinstanceからも呼ばれるので
        if hasattr(cls, '__name__'):
            return '%s/%s/' % (cls.__name__, pk)
        else:
            return '%s/%s/' % (cls.__class__.__name__, pk)

    @classmethod
    def get_cache_all_path(cls):
        # classmethodはclassからもinstanceからも呼ばれるので
        if hasattr(cls, '__name__'):
            return '%s/all/' % (cls.__name__)
        else:
            return '%s/all/' % (cls.__class__.__name__)

    @classmethod
    def get_cache(cls, pk):
        cache_path = cls.get_cache_path(pk)
        model = cache.get(cache_path, None)
        if model is None:
            try:
                model = cls.objects.get(pk=pk)
                cache.set(cache_path, model, (3600 * 24))
            except cls.DoesNotExist:
                pass
        return model

    @classmethod
    def get_cache_all(cls):
        cache_path = cls.get_cache_all_path()
        models = cache.get(cache_path, None)
        if models is None:
            models = list(cls.objects.all())
            cache.set(cache_path, models, (3600 * 24))
        return models
