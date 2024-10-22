from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def index(req):
    return render(req,'index.html')
def main(req):
    
    return render(req, 'main.html')
