from unittest import mock
from attr import attr
from django import forms
from .models import Todo

class CreateTodoForm(forms.ModelForm):
  title = forms.CharField(
    label='Title',
    widget=forms.TextInput(
      attrs={
        "placeholder": "todo title"
      }
    )
  )
  description = forms.CharField(
    label="Description",
    widget=forms.Textarea(
      attrs={
        "placeholder": "todo description"
      }
    )
  )
  limit_date = forms.DateTimeField(
    label="Limit date"
  )
  class Meta:
    model = Todo
    fields = [
      "title",
      "description",
      "limit_date"
    ]