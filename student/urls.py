from django.urls import path, include
from student.views import student_index

urlpatterns = [
    path('', student_index, name='student_index'),

]