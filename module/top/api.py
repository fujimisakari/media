# -*- coding: utf-8 -*-

from django.core.cache import cache
from module.top.models import WhatNew


def create_whatnew(data_list):
    for data in data_list:
        WhatNew.objects.create(
            create_date=data['create_date'],
            content=data['content'],
        )


def edit_whatnew(edit_data_list):
    for data in edit_data_list:
        whatnew = WhatNew.objects.select_for_update().get(id=data['id'])
        whatnew.create_date = data['create_date']
        whatnew.content = data['content']
        whatnew.save()


def delete_whatnew_cache(id_list):
    for del_id in id_list:
        cache.delete(WhatNew.get_cache_path(del_id))
    cache.delete(WhatNew.get_cache_all_path())
