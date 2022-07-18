from django.db import models
from django.urls import reverse

class Diary(models.Model):
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse("crud:detail", kwargs={"pk": self.pk})
    
    
    
