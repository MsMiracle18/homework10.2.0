from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="root"),
    path("page/<int:page>/", views.main, name="root_paginate"),
    path('registration/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


    
