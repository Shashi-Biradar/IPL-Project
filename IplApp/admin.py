from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Franchise)
admin.site.register(models.Player)
admin.site.register(models.Stadium)
admin.site.register(models.Profile)