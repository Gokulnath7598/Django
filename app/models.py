from django.db import models

class Bio (models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    Date=models.DateField()
