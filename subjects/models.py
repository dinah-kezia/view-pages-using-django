from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField(default="No content available")  
    image = models.ImageField(upload_to='media/subject_images/')

    def __str__(self):
        return self.name

class Content(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
