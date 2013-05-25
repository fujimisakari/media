# -*- coding: utf-8 -*-

# メッセージ一覧
MSG_ADD = '登録しました'
MSG_EDIT = '編集しました'
MSG_DELET = '削除しました'
MSG_CHECKED_DELET = 'チェック項目を削除しました'
ERROR_MSG_ADD = '入力値が正常でないため、登録が行えませんでした'
ERROR_MSG_EDIT = '入力値が正常でないため、編集が行えませんでした'
ERROR_MSG_FILEPATH = 'カテゴリまたはサブカテゴリの組み合わせが正しくありません'
MSG_UPLOAD = 'アップロードしました'
ERROR_MSG_UPLOAD_FILEPATH = 'カテゴリ、サブカテゴリ、タイトルの組み合わせが正しくありません'
ERROR_MSG_UPLOAD = '入力値が正常でないため、アップロードが行えませんでした'


def titleSelecter(type, value):
    # 管理画面のタイトル設定
    title_list = {'top': {'whatnew': '[TOP] What New'},
                  'book': {'entry': '[BOOK] タイトル',
                           'detail': '[BOOK] タイトル詳細',
                           'category': '[BOOK] カテゴリ',
                           'subcategory': '[BOOK] サブカテゴリ',
                           'writer': '[BOOK] 著者',
                           'publisher': '[BOOK] 出版社'},
                  'upload': {'book': '[UPLOAD] BOOK'},
                  'analysis': {'book': '[ANALYSIS] BOOK',
                               'movie': '[ANALYSIS] MOVIE',
                               'music': '[ANALYSIS] MUSIC'},
                  }
    title_list[type][value]
    return title_list[type][value]
