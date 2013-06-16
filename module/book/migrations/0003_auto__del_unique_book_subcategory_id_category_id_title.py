# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Book', fields ['subcategory_id', 'category_id', 'title']
        db.delete_unique('book_book', ['subcategory_id', 'category_id', 'title'])

        # Adding index on 'Book', fields ['category_id']
        db.create_index('book_book', ['category_id'])


    def backwards(self, orm):
        # Removing index on 'Book', fields ['category_id']
        db.delete_index('book_book', ['category_id'])

        # Adding unique constraint on 'Book', fields ['subcategory_id', 'category_id', 'title']
        db.create_unique('book_book', ['subcategory_id', 'category_id', 'title'])


    models = {
        'book.book': {
            'Meta': {'object_name': 'Book'},
            'category_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subcategory_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'book.bookdetail': {
            'Meta': {'unique_together': "(('book_id', 'volume'),)", 'object_name': 'BookDetail'},
            'book_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
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
            'Meta': {'unique_together': "(('category_id', 'name'),)", 'object_name': 'SubCategory'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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