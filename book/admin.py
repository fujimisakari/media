# -*- coding: utf-8 -*-

from django.contrib import admin
from book.models import Category, SubCategory, Book, BookDetail, Writer, Publisher


class CategoryOptions(admin.ModelAdmin):
    list_display = ('name', 'url',)


class SubCategoryOptions(admin.ModelAdmin):
    list_display = ('category', 'name', 'url',)
    ordering = ('-name',)


class BookOptions(admin.ModelAdmin):
    list_display = ('category', 'subcategory', 'title', 'url_title',)
    list_filter = ('category', 'subcategory',)
    # search_fields = ('title', 'url_title',)

    fieldsets = (
        (None, {
            'fields': ('category', 'subcategory', ('title', 'url_title',),)
        }),
    )


class WriterOptions(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class PublisherOptions(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class BookDetailOptions(admin.ModelAdmin):
    list_display = ('entry', 'volume', 'pdf_size', 'epud_size', 'total_page',
                    'writer', 'publisher', 'description', 'exit_pdf', 'exit_epud',)
    list_filter = ('entry', 'writer', 'publisher',)
    # search_fields = ('entry', 'writer', 'publisher', 'description',)

    fieldsets = (
        (None, {
            'fields': ('entry', 'volume', ('pdf_size', 'exit_pdf',), ('epud_size', 'exit_epud',),
                       'total_page', 'writer', 'publisher', 'description',)
        }),
    )

admin.site.register(Category, CategoryOptions)
admin.site.register(SubCategory, SubCategoryOptions)
admin.site.register(Book, BookOptions)
admin.site.register(Writer, WriterOptions)
admin.site.register(Publisher, PublisherOptions)
admin.site.register(BookDetail, BookDetailOptions)
