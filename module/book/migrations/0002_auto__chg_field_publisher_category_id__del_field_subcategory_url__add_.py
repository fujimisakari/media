# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Publisher.category_id'
        db.alter_column('book_publisher', 'category_id', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Deleting field 'SubCategory.url'
        db.delete_column('book_subcategory', 'url')

        # Adding field 'SubCategory.url_name'
        db.add_column('book_subcategory', 'url_name',
                      self.gf('django.db.models.fields.CharField')(default=1, unique=True, max_length=100),
                      keep_default=False)


        # Changing field 'Writer.category_id'
        db.alter_column('book_writer', 'category_id', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Deleting field 'Category.url'
        db.delete_column('book_category', 'url')

        # Adding field 'Category.url_name'
        db.add_column('book_category', 'url_name',
                      self.gf('django.db.models.fields.CharField')(default=1, unique=True, max_length=100),
                      keep_default=False)

        # Deleting field 'Book.url'
        db.delete_column('book_book', 'url')

        # Adding field 'Book.url_name'
        db.add_column('book_book', 'url_name',
                      self.gf('django.db.models.fields.CharField')(default=1, unique=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Publisher.category_id'
        raise RuntimeError("Cannot reverse this migration. 'Publisher.category_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SubCategory.url'
        raise RuntimeError("Cannot reverse this migration. 'SubCategory.url' and its values cannot be restored.")
        # Deleting field 'SubCategory.url_name'
        db.delete_column('book_subcategory', 'url_name')


        # User chose to not deal with backwards NULL issues for 'Writer.category_id'
        raise RuntimeError("Cannot reverse this migration. 'Writer.category_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Category.url'
        raise RuntimeError("Cannot reverse this migration. 'Category.url' and its values cannot be restored.")
        # Deleting field 'Category.url_name'
        db.delete_column('book_category', 'url_name')


        # User chose to not deal with backwards NULL issues for 'Book.url'
        raise RuntimeError("Cannot reverse this migration. 'Book.url' and its values cannot be restored.")
        # Deleting field 'Book.url_name'
        db.delete_column('book_book', 'url_name')


    models = {
        'book.book': {
            'Meta': {'object_name': 'Book'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subcategory_id': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'url_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
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
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
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
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'book.writer': {
            'Meta': {'object_name': 'Writer'},
            'category_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['book']