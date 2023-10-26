from django import forms

class Cmmentform(forms.ModelForm):
  class Meta:
    model = ""
    fields = ["name", "email", "body"]