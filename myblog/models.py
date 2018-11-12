from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class Articles(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    # last_update_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    # 关联另一个表的主键
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    # 标记是否是删除，而不是从数据库中真正删除
    is_deleted = models.BooleanField(default=False)
    # 阅读数量一般不是这样实现的
    readed_num = models.IntegerField(default=0)

    # def __str__(self):
    #     return "<Articles: {}>".format(self.title)


class Comments(models.Model):
    time = models.TimeField()
    content = models.TextField()
