from django.db import models

# Create your models here.
"""
系统会自动添加主键--id
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=20)


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
