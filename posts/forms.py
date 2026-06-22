from django import forms
from .models import Post

class PostForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(max_value=9999999999, required=False)