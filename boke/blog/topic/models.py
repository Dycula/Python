from django.db import models

# Create your models here.
from user.models import UserProfile


class Topic(models.Model):

  title = models.CharField(max_length=90, verbose_name="文章主题")
  #'tec' - 技术类    'no-tec' - 非技术类
  category = models.CharField(max_length=20,verbose_name="文章分类")
  # 'public' - 公开的   'private' - 私有的
  limit = models.CharField(max_length=10, verbose_name="文章权限")
  introduce = models.CharField(max_length=90, verbose_name="文章简介")
  content = models.TextField(verbose_name="文章内容")
  created_time = models.DateTimeField(auto_now_add=True)
  modified_time = models.DateTimeField(auto_now=True)
  #外键
  author = models.ForeignKey(UserProfile)

  class Meta:
    db_table = 'topic'










