# -*- coding: utf-8 -*-
import sys, re
from ctypes import *
from django.conf import settings

def search_index(keyword):
    # enums were in 'estraier.h'
    ESTDBREADER = 1

    est = CDLL("libestraier.so.8")

    ecode = c_int()

    # データベースを開く
    db = est.est_db_open( settings.HYPER_ESTRAIER_INDEX, ESTDBREADER, byref(ecode))
    if not db:
        func = est.est_err_msg
        func.restype = c_char_p
        print >>sys.stderr, "error: %s" % func(ecode)
        sys.exit(1)

    # 検索条件オブジェクトを生成する
    cond = est.est_cond_new()

    # 検索条件オブジェクトに検索式を設定する
    est.est_cond_set_phrase(cond, keyword)

    # データベースから検索結果を得る
    func = est.est_db_search
    func.restype = POINTER(c_int) # int *は基本型としては定義されてない
    resnum = c_int()
    result = func(db, cond, byref(resnum), None)

    result_list  = []

    # 各該当文書を取得して表示する
    for i in xrange(0, resnum.value):

        search_result = {}

        # 文書オブジェクトを取得する
        doc = est.est_db_get_doc(db, result[i], 0)
        if not doc:
            continue

        # ファイルパスを取得
        func = est.est_doc_attr
        func.restype = c_char_p
        value = func(doc, "@uri")
        if value:
            text_list = value.split('/')
            search_result['uri'] = '%s/%s/%s/' % (text_list[-4], text_list[-3], text_list[-2])

        # 本文を取得
        texts = est.est_doc_texts(doc)
        text_join = ''
        for j in xrange(0, est.cblistnum(texts)):
            func = est.cblistval
            func.restype = c_char_p
            value = func(texts, j, None)
            # print "%s" % value
            text_join += value + ' '
        search_result['content'] = text_join

        result_list.append(search_result)

        # 文書オブジェクトを破壊する
        est.est_doc_delete(doc)

    # 検索結果を破壊する
    libc = CDLL("libc.so.6")
    libc.free(result)

    # 検索条件オブジェクトを破棄する
    est.est_cond_delete(cond)

    # データベースを閉じる
    res = est.est_db_close(db, byref(ecode))
    if not res:
        func = est.est_err_msg
        func.restype = c_char_p
        print >>sys.stderr, "error: %s" % func(ecode)
        sys.exit(1)

    return result_list
