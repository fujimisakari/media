# -*- coding: utf-8 -*-

import re
import os
import sys
import glob

from django.conf import settings
from django.db import connection
from django.db.models import get_app, get_models
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

        csv_dir_path = '{}*'.format(settings.CSV_DATA_PATH)
        csv_file_list = glob.glob(csv_dir_path)
        for csv_file in csv_file_list:
            os.remove(csv_file)

        p = r"(django|south)"
        r = re.compile(p)
        cur = connection.cursor()
        for app_name in settings.INSTALLED_APPS:
            if not r.match(app_name):
                for model in get_models(get_app(app_name)):
                    csv_file_path = '{}{}.csv'.format(settings.CSV_DATA_PATH, model._meta.db_table)
                    try:
                        export_sql = "SELECT * FROM {} INTO OUTFILE '{}' fields terminated by ','".format(model._meta.db_table, csv_file_path)
                        cur.execute(export_sql)
                    except Warning:
                        print >> sys.stderr, u"not exist '{}'.".format(model._meta.db_table)
