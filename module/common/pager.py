# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage


def get_pager(query_set, page=1, limit=15):
    paginator = Paginator(query_set, limit)
    try:
        p = paginator.page(page)
    except InvalidPage:
        p = paginator.page(1)

    if len(paginator.page_range) > 25:
        current_page = p.number
        before_offset = 0
        after_offset = 0
        for offset in paginator.page_range[0:len(paginator.page_range):25]:
            if offset > current_page:
                after_offset = offset
                break
            before_offset = offset
        before_offset -= 1
        if after_offset:
            after_offset -= 1
            page_range = paginator.page_range[before_offset:after_offset]
        else:
            page_range = paginator.page_range[before_offset:]
    else:
        page_range = paginator.page_range

    pager = {
        'total': paginator.count,
        'page_range': page_range,
        'start_index': p.start_index(),
        'end_index': p.end_index(),
        'current_page': p.number,
        'has_previous': p.has_previous(),
        'has_next': p.has_next(),
        'previous_page': p.previous_page_number(),
        'next_page': p.next_page_number(),
    }
    return pager, p.object_list
