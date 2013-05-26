# -*- coding: utf-8 -*-

import re
import os
import sys

from django.conf import settings
from django.db import connection, transaction
from django.db.models import get_app, get_models
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

        p = r"(django|south)"
        r = re.compile(p)
        cur = connection.cursor()
        for app_name in settings.INSTALLED_APPS:
            if not r.match(app_name):
                app_name = app_name.replace('module.', '')
                for model in get_models(get_app(app_name)):
                    csv_file_path = '{}{}.csv'.format(settings.CSV_DATA_PATH, model._meta.db_table)
                    is_exist = os.path.exists(csv_file_path)
                    if is_exist:
                        try:
                            cur.execute("TRUNCATE {}".format(model._meta.db_table))
                            import_sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE {} FIELDS TERMINATED BY ','".format(csv_file_path, model._meta.db_table)
                            cur.execute(import_sql)
                            transaction.commit_unless_managed()
                        except Warning:
                            print >> sys.stderr, u"not exist '{}'.".format(model._meta.db_table)
