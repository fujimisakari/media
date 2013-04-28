# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WhatNew'
        db.create_table('top_whatnew', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('regist_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('top', ['WhatNew'])


    def backwards(self, orm):
        # Deleting model 'WhatNew'
        db.delete_table('top_whatnew')


    models = {
        'top.whatnew': {
            'Meta': {'object_name': 'WhatNew'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'regist_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['top']