# -*- coding: utf-8 -*-

import sys
from django.conf import settings
from django.core.management import call_command, load_command_class
from django.core.management.base import BaseCommand
from django.db import connection
from django.db.models import get_app, get_models
from south.models import MigrationHistory
from _mysql_exceptions import Warning


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            app_name = args[0]
        except IndexError:
            print >> sys.stderr, 'Please input app_name.'
            return

        app_name_list = [_app_name.replace('module.', '') for _app_name in settings.INSTALLED_APPS]
        if not app_name in app_name_list:
            print >> sys.stderr, 'Please input valid app_name.'
            return
        print >> sys.stderr, u'database: {}'.format(connection.alias)

        cur = connection.cursor()
        MigrationHistory.objects.using(connection.alias).filter(app_name=app_name).delete()
        for model in get_models(get_app(app_name)):
            try:
                cur.execute('DROP TABLE IF EXISTS {} CASCADE'.format(model._meta.db_table))
            except Warning:
                print >> sys.stderr, u"not exist '{}'.".format(model._meta.db_table)
        cur.close()
        call_command('migrate', app_name, database=connection.alias, delete_ghosts=True)

        print 'import csv data start.'
        klass = load_command_class('module.common', 'importcsv')
        klass.execute()
        print 'import csv data done.'
