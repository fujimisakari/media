# -*- coding: utf-8 -*-

from django import forms
from module.top.models import WhatNew
from module.book.models import Category, SubCategory, Book, BookDetail, Writer, Publisher


class WhatNewForm(forms.ModelForm):
    class Meta:
        model = WhatNew


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
