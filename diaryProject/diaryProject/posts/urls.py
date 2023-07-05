from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts import views

app_name = "posts"

urlpatterns = [
     path('', views.home, name='home'),
     path('post_list/', views.post_list, name='post_list'),
     path('create/', views.create, name='create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)