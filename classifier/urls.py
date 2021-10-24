from django.urls import path
from classifier import views

urlpatterns = [
    path('classification', views.classification, name='classification'),
]
