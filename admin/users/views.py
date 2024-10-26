from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Login(req):
    return render(req, 'Login.html')
