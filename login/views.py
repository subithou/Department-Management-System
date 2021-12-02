from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

import home_page.views
import student.views
from login.form import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from login.models import login_table


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = login_table.objects.filter(username=username, password=password, category='student')
        print(user, username)
        if not user:
            messages.error(request, 'username or password not correct')
            return redirect('login')

        else:
            # if user.is_active:

            return redirect(student.views.student_index)
        # return redirect(student.views.student_index)

    return render(request, 'login.html')
