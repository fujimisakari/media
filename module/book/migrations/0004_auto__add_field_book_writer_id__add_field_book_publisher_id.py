# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.writer_id'
        db.add_column('book_book', 'writer_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Book.publisher_id'
        db.add_column('book_book', 'publisher_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.writer_id'
        db.delete_column('book_book', 'writer_id')

        # Deleting field 'Book.publisher_id'
        db.delete_column('book_book', 'publisher_id')


    models = {
        'book.book': {
            'Meta': {'object_name': 'Book'},
            'category_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'subcategory_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'writer_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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
            'volume': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
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