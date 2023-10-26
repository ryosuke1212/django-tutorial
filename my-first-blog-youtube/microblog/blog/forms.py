from django import forms
from .models import Comment

class Cmmentform(forms.ModelForm):
  class Meta:
    model = Comment
    model = ""
    fields = ["name", "email", "body"]