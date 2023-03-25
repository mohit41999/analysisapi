from django.db import models

# Create your models here.

class Field(models.Model):
    # id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    Company = models.CharField(max_length=200)
    Role = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)
    InternshipDuration = models.CharField(max_length=200, default='SOME STRING')
    Intake = models.CharField(max_length=200)