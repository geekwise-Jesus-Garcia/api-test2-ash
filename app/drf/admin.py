# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Branch, Customer, Account, Product

Register your models here.
admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Product)