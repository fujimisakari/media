# -*- coding: utf-8 -*-

from django import forms
from django.forms.formsets import formset_factory
from module.book.models import Category, SubCategory, Book, BookDetail, Writer, Publisher


class WhatNewForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    create_date = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'date_input text', 'name': 'date', 'tabindex': '13'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': '5', 'cols': '50', 'tabindex': '12'}))


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory


class BookForm(forms.ModelForm):
    class Meta:
        model = Book


class BookDetailForm(forms.ModelForm):
    class Meta:
        model = BookDetail


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher


WhatNewFormSet = formset_factory(WhatNewForm, max_num=1)
