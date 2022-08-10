from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Diary(models.Model):
    pub_date = models.DateTimeField('date published',auto_now=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    #user = models.ForeignKey(User,on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.title
    
    
    
