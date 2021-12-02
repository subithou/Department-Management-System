from django.urls import path, include
from home_page.views import home

urlpatterns = [
    path('', home, name='home'),
    ]