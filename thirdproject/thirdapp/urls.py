from django.contrib import admin
from django.urls import path
from thirdapp import views

urlpatterns = [

    path('hello/',views.hello_world),
    path('time/',views.time_given)
]
