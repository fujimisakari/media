# -*- coding: utf-8 -*-

from django import forms
from django.forms.formsets import formset_factory


class WhatNewForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    create_date = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'date_input text', 'name': 'date', 'tabindex': '13'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': '5', 'cols': '50', 'tabindex': '12'}))


class CategoryForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '7'}))
    sort = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '2', 'maxlength': '3'}))


class SubCategoryForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    category_id = forms.IntegerField()
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '7'}))
    sort = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '2', 'maxlength': '3'}))


class BookForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    category_id = forms.IntegerField()
    subcategory_id = forms.IntegerField()
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '7'}))
    writer_id = forms.IntegerField()
    publisher_id = forms.IntegerField()


class BookDetailForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    book_id = forms.IntegerField()
    volume = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '2', 'maxlength': '3'}))
    pdf_size = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '2', 'maxlength': '3'}))
    # epud_size = forms.IntegerField()
    total_page = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text size1', 'tabindex': '2', 'maxlength': '4'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': '5', 'cols': '50', 'tabindex': '12'}))
    # exit_pdf = forms.BooleanField()
    # exit_epud = forms.BooleanField()
    exit_attachment = forms.BooleanField(required=False)


class WriterForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    category_id = forms.IntegerField()
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '7'}))


class PublisherForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    category_id = forms.IntegerField()
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text size4', 'tabindex': '7'}))


WhatNewFormSet = formset_factory(WhatNewForm, max_num=1)
CategoryFormSet = formset_factory(CategoryForm, max_num=1)
SubCategoryFormSet = formset_factory(SubCategoryForm, max_num=1)
BookFormSet = formset_factory(BookForm, max_num=1)
BookDetailFormSet = formset_factory(BookDetailForm, max_num=1)
WriterFormSet = formset_factory(WriterForm, max_num=1)
PublisherFormSet = formset_factory(PublisherForm, max_num=1)
