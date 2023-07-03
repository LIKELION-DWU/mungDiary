from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')), # accounts 앱 urls에서 직접관리
]
