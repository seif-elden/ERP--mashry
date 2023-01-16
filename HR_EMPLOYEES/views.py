from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hr_emp_home(request):
    return HttpResponse("welcome from django hr_emp_home")