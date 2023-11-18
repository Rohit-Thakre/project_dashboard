from django.contrib import admin
from main import models
# Register your models here.


@admin.register(models.Data)
class AdminUser(admin.ModelAdmin):
    list_display = ['id', 'end_year', 'intencity',  'topic', 'insight', 'url', 'region', 'start_year']



@admin.register(models.Country)
class AdminCountry(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Sector)
class AdminSector(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Region)
class AdminRegion(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Pestle)
class AdminPestle(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Topic)
class AdminTopic(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Source)
class AdminSource(admin.ModelAdmin):
    list_display = ['id', 'name']


