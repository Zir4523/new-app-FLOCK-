from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
# Create your models here.

class Memo(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=100)
    text = models.TextField(verbose_name='内容')
    created_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    def __str__(self):
        return self.title
        
class Todo(models.Model): 
    todo = models.CharField('ToDo', max_length=100, blank=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)

    def __str__(self):
        return self.todo