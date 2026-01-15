from django.db import models

# Create your models here.

class JobDescription(models.Model):
    role = models.CharField(max_length=100)
    description = models.TextField()

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    score = models.FloatField(default=0)

