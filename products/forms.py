from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Company

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='this field is required')
    first_name = forms.CharField(required=True, label="Ваше имя", max_length=254)
    class Meta:
        model = User
        fields = ('first_name','username', 'email', 'password1', 'password2', )
class ProductForm(forms.Form):
    title = forms.CharField(required=True, label="Название *", widget = forms.TextInput(
        attrs = {
            "placeholder" : "Название продукта"
        }
    ))
    description = forms.CharField(required=True, label="Описание *",
                                  widget = forms.Textarea(
                                      attrs = {
                                          "paceholder" : "Описание продукта",
                                          "rows": 5,
                                          "cols": 30
                                      }
                                  ))
    weight = forms.CharField(required=True, label="Вес *")
    company = forms.ModelChoiceField(queryset=Company.objects.all(),label="Компания *")