from django import forms
from top.models import WhatNew
from book.models import Category, SubCategory, Entry, Entry_Detail, Writer, Publisher

class WhatNewForm(forms.ModelForm):
    class Meta:
        model = WhatNew

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry

class Entry_DetailForm(forms.ModelForm):
    class Meta:
        model = Entry_Detail

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
