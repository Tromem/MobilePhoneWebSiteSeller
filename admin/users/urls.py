from django.urls import path,include 
from .views import Login

urlpatterns = [
   path('log',Login),
]