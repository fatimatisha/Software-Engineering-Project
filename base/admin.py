from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(userAccount)

"""
model: userAccount- for storing user informations
model: solutionCode- for storing solution codes
"""

admin.site.register(solutionCode)