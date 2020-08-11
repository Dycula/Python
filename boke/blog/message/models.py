from django.db import models
from topic.models import Topic
from user.models import UserProfile

# Create your models here.
class Message(models.Model):
  #Topic外键
  topic = models.ForeignKey(Topic)
  #UserProfile外键
  publisher = models.ForeignKey(UserProfile)
  content = models.CharField(max_length=90, verbose_name='内容')
  created_time = models.DateTimeField(auto_now_add=True)
  #父级Message id, 默认为0; 0->留言 非0->回复
  parent_message = models.IntegerField(default=0)

  class Meta:
    db_table = 'message'










