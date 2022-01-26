from dataclasses import fields
from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        exclude = []