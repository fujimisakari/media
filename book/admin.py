from django.contrib import admin
from book.models import Category, SubCategory, Entry, Entry_Detail, Writer, Publisher

class CategoryOptions(admin.ModelAdmin):
    list_display = ('name', 'url_name',)

class SubCategoryOptions(admin.ModelAdmin) :
    list_display = ('category', 'name', 'url_name',)
    ordering = ('-name',)


class EntryOptions(admin.ModelAdmin) :
    list_display = ('category', 'subcategory', 'title', 'url_title',)
    list_filter = ('category','subcategory',)
    # search_fields = ('title', 'url_title',)

    fieldsets = (
        (None, {
            'fields': ('category', 'subcategory', ('title', 'url_title',),)
        }),
    )

class WriterOptions(admin.ModelAdmin) :
    list_display = ('name',)
    ordering = ('name',)

class PublisherOptions(admin.ModelAdmin) :
    list_display = ('name',)
    ordering = ('name',)

class Entry_DetailOptions(admin.ModelAdmin) :
    list_display = ('entry', 'volume', 'pdf_size', 'epud_size', 'total_page',
                    'writer', 'publisher', 'description', 'exit_pdf', 'exit_epud',)
    list_filter = ('entry', 'writer', 'publisher',)
    # search_fields = ('entry', 'writer', 'publisher', 'description',)

    fieldsets = (
        (None, {
            'fields': ('entry', 'volume', ('pdf_size', 'exit_pdf',),('epud_size', 'exit_epud',),
                       'total_page', 'writer', 'publisher', 'description',)
        }),
    )

admin.site.register(Category, CategoryOptions)
admin.site.register(SubCategory, SubCategoryOptions)
admin.site.register(Entry, EntryOptions)
admin.site.register(Writer, WriterOptions)
admin.site.register(Publisher, PublisherOptions)
admin.site.register(Entry_Detail, Entry_DetailOptions)
