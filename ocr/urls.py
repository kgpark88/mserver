from django.urls import path
from ocr import views

urlpatterns = [
    path('ocr', views.ocr, name='ocr'),
]
