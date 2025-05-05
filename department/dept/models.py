from django.db import models
from datetime import date
# Create your models here.
class add_department(models.Model):
    Department_Name = models.CharField(max_length=250)
    Department_description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)