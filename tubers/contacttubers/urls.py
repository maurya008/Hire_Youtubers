from django.urls import path

from . import views

urlpatterns = [
    path('contacttuber', views.contacttuber, name="contacttuber"),
    
]