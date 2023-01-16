from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hr_payroll_home(request):
    return HttpResponse("welcome from django hr_payroll_home")