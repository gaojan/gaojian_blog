#!/usr/bin/env python
# encoding: utf-8
from django.contrib import admin

# Register your models here.
from .models import OwnTrackLog


class OwnTrackLogsAdmin(admin.ModelAdmin):
    pass
