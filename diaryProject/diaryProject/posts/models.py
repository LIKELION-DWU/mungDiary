from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='diary-photo')
    body = models.TextField(verbose_name="내용", default="")
    writer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # 작성일가져오기
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    comment_count = models.IntegerField(verbose_name="댓글수", default=0)

    def __str__(self):
        return self.body

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.comment
