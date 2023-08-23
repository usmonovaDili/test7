from django import forms
from .models import User


class UserForms(forms.ModelForm):
    name_uz = forms.CharField()
    name_en = forms.CharField(required=False)
    name_ru = forms.CharField(required=False)

    lastname_uz = forms.CharField()
    lastname_en = forms.CharField(required=False)
    lastname_ru = forms.CharField(required=False)

    username_uz = forms.CharField()
    username_en = forms.CharField(required=False)
    username_ru = forms.CharField(required=False)

    class Meta:
        model = User
        exclude = ['name', 'lastname', 'username']
