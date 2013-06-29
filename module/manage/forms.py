# -*- coding: utf-8 -*-

from django import forms
from django.forms.formsets import formset_factory
from module.book.models import BookDetail


class WhatNewForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    create_date = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'date_input text', 'name': 'date', 'tabindex': '1'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': '5', 'cols': '50', 'tabindex': '2'}))


class CategoryForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '1'}))
    sort = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '2', 'maxlength': '3'}))


class SubCategoryForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    category_id = forms.IntegerField()
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '2'}))
    sort = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '3', 'maxlength': '3'}))


class BookForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    category_id = forms.IntegerField()
    subcategory_id = forms.IntegerField()
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '3'}))
    writer_id = forms.IntegerField()
    publisher_id = forms.IntegerField()


class BookDetailForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    book_id = forms.IntegerField()
    volume = forms.IntegerField(required=False)
    pdf_size = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '5', 'maxlength': '3'}))
    # epud_size = forms.IntegerField()
    total_page = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '6', 'maxlength': '4'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': '5', 'cols': '50', 'tabindex': '8'}))
    # exit_pdf = forms.BooleanField()
    # exit_epud = forms.BooleanField()
    exit_attachment = forms.BooleanField(required=False)

    def clean_volume(self):
        detail_id = self.cleaned_data['id']
        book_id = self.cleaned_data['book_id']
        volume = self.cleaned_data['volume']
        if detail_id:
            # volumeの重複チェック
            book_detail_list = BookDetail.get_book_detail_list_by_book_id(book_id)
            if [bd for bd in book_detail_list if bd.volume == volume]:
                raise forms.ValidationError(u'volumeが重複してます')
        if volume:
            # 空の場合はデフォルト値を入れる
            self.cleaned_data['volume'] = 1


class WriterForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    category_id = forms.IntegerField()
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '2'}))


class PublisherForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    category_id = forms.IntegerField()
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '2'}))


WhatNewFormSet = formset_factory(WhatNewForm, max_num=1)
CategoryFormSet = formset_factory(CategoryForm, max_num=1)
SubCategoryFormSet = formset_factory(SubCategoryForm, max_num=1)
BookFormSet = formset_factory(BookForm, max_num=1)
BookDetailFormSet = formset_factory(BookDetailForm, max_num=1)
WriterFormSet = formset_factory(WriterForm, max_num=1)
PublisherFormSet = formset_factory(PublisherForm, max_num=1)
