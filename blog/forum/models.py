from django.db import models

# Create your models here.
class Post(models.Model):
    Topic = models.CharField(max_length=256, verbose_name='Тема')
    Text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.Topic

    def get_comments(self):
        return self.post_comment.all()

class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE, verbose_name='Связанный пост')

    def __str__(self):
        return self.text