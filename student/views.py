from django.shortcuts import render


# Create your views here.
def student_index(request):
    return render(request, 'student_index.html')
