from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


class ReunionModel(ModelAdmin):
    list_display = ['Title', 'Date', 'Place']
    search_fields = ['Title']
    list_filter = ['Date']


admin.site.register(Reunion, ReunionModel)


class WebinarModel(ModelAdmin):
    list_display = ['Title', 'Date']
    search_fields = ['Title', 'Memo']
    list_filter = ['Date']


admin.site.register(Webinar, WebinarModel)