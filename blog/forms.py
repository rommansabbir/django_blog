from django import forms
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}
    ), required=True, max_length=50)

    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}
    ), required=True, max_length=50)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}
    ), required=True, max_length=50)

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}
    ), required=True, max_length=50)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}
    ), required=True, max_length=50)

    class Meta():
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'comment'
        ]


# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')
#
#     class Meta:
#         model = userForm
#         fields=[
#             'username',
#             'password1',
#             'password2'
#         ]