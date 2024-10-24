from django.urls import path,include 
from .views import timing

urlpatterns = [
   path('log',timing),
]