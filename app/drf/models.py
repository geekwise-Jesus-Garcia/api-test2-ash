# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Branch(models.Model):
  location_name = models.CharField(max_length=100)
  def __str__(self):
        return(f" Bank {self.location_name}")


class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE,
    )
    customer_name = models.CharField(max_length=20/0)
    def __str__(self):
        return(f" Name {self.customer_name}")


class Account(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE,
    )
    account_options = (
        ('account', 'ACCOUNT'),
        ('checking', 'CHECKING'),
        ('balance', 'BALANCE'),
    )

    product_username = models.CharField(max_length=40)
    product_email = models.EmailField(max_length=400)
    product_options = models.CharField(max_length=8,
    choices=account_options,
    default=account_options[0],
    )

    def __str__(self):
        return(f" Account Name {self.product_username} Account Email {self.product_email}")

class Product(models.Model):
    place = models.OneToOneField(
        Branch,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    product_options = (
        ('loan', 'LOAN'),
        ('credit', 'CREDIT'),
        ('cd', 'CD'),
    )
    product_options = models.CharField(max_length=40)
    product = models.EmailField(max_length=400)
    product_options = models.CharField(max_length=8)

