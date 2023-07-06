from django.contrib import admin
from django.urls import path, include
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('', views.login, name='login'), # http://127.0.0.1:8000/accounts/
    path('signup/', views.signup, name='signup'), # 회원가입
    path('logout/', views.logout, name='logout'), # 로그아웃
]