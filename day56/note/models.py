from django.db import models

# Create your models here.
from user.models import User
class Note(models.Model):
    title=models.CharField("标题",max_length=30)
    content=models.TextField("内容")
    create_time=models.DateTimeField("创建时间",auto_now_add=True)
    mod_time=models.DateTimeField("修改时间",auto_now_add=True)
    user=models.ForeignKey(User)