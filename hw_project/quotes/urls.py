from django.urls import path
from . import views

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="root"),
    path("page/<int:page>/", views.main, name="root_paginate"),
    path('registration/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
]

