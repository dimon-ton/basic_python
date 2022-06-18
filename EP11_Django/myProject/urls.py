from django.urls import path
from myProjectApp.views import hello

urlpatterns = [
   path('', hello)
]
