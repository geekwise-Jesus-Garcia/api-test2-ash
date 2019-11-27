# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Branch(models.Model):
    location_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

def __str__(self):
    return(f"Bank {self.location_name}")

#   def __str__(self):
#     return(f" Bank Name {self.location_name} - location{self.location}")