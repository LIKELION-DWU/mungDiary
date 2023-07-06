from django.contrib import admin
from .models import Post, Comment

# models에게 Post, Comment를 등록했다는 것을 알려주기 위한 작업
admin.site.register(Post)
admin.site.register(Comment)
