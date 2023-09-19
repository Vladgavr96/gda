from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=60)
    phone = models.IntegerField()
    email = models.EmailField()
    comment = models.TextField()