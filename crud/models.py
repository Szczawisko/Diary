from django.db import models

class Diary(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=255)
    body = models.TextField()
