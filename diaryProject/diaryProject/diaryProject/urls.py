from django.contrib import admin
from django.urls import path, include
from accounts import views
from posts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('accounts.urls', namespace='accounts')), # accounts 앱 urls에서 직접관리
    path('posts/', include('posts.urls', namespace='posts')),  # posts 앱 urls에서 직접관리
]
