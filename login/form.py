from django import forms

from login.models import login_table


class LoginForm:
    class meta:
        model = login_table
        fields = ['username', 'password', 'category']

