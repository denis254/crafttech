from django.db import models
import datetime
from django.utils import timezone

class contactusa(models.Model):

    published_date = models.DateTimeField(auto_now_add=True, null = "True", blank = "True")
    Full_Name = models.CharField(max_length=300)
    Email = models.CharField(max_length=300)
    Phone_Number = models.CharField(max_length=300)
    Country = models.CharField(max_length=300)
    Type_of_Project = models.CharField(max_length=300)
    Estimated_budget = models.CharField(max_length=300)
    Tell_Us_About_Your_Project = models.CharField(max_length=300)

    def __str__(self):  # __unicode__ for Python 2
        return self.Type_of_Project
