# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('book_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('book', ['Category'])

        # Adding model 'SubCategory'
        db.create_table('book_subcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('book', ['SubCategory'])

        # Adding model 'Book'
        db.create_table('book_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_id', self.gf('django.db.models.fields.IntegerField')()),
            ('subcategory_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('book', ['Book'])

        # Adding model 'BookDetail'
        db.create_table('book_bookdetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_id', self.gf('django.db.models.fields.IntegerField')()),
            ('volume', self.gf('django.db.models.fields.IntegerField')()),
            ('pdf_size', self.gf('django.db.models.fields.IntegerField')()),
            ('epud_size', self.gf('django.db.models.fields.IntegerField')()),
            ('total_page', self.gf('django.db.models.fields.IntegerField')()),
            ('writer_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('publisher_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('exit_pdf', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('exit_epud', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('exit_attachment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('book', ['BookDetail'])

        # Adding model 'Writer'
        db.create_table('book_writer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('book', ['Writer'])

        # Adding model 'Publisher'
        db.create_table('book_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('book', ['Publisher'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('book_category')

        # Deleting model 'SubCategory'
        db.delete_table('book_subcategory')

        # Deleting model 'Book'
        db.delete_table('book_book')

        # Deleting model 'BookDetail'
        db.delete_table('book_bookdetail')

        # Deleting model 'Writer'
        db.delete_table('book_writer')

        # Deleting model 'Publisher'
        db.delete_table('book_publisher')


    models = {
        'book.book': {
            'Meta': {'object_name': 'Book'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subcategory_id': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'book.bookdetail': {
            'Meta': {'object_name': 'BookDetail'},
            'book_id': ('django.db.models.fields.IntegerField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'epud_size': ('django.db.models.fields.IntegerField', [], {}),
            'exit_attachment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exit_epud': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exit_pdf': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf_size': ('django.db.models.fields.IntegerField', [], {}),
            'publisher_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'total_page': ('django.db.models.fields.IntegerField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {}),
            'writer_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'book.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'book.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'category_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'book.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'book.writer': {
            'Meta': {'object_name': 'Writer'},
            'category_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['book']