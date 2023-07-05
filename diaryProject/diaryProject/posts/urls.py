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
     path('post_list/', views.post_list, name='post_list'),
     path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
     
     path('create_comment/<int:id>', views.create_comment, name='create_comment'),
     path('update_comment/<int:post_id>/<int:com_id>', views.update_comment, name='update_comment'),
     path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment, name='delete_comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)