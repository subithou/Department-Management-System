from django.urls import path, include
from login.views import login

urlpatterns = [
    path('', login, name='login'),

]
