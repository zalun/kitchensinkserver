"""
device.admin
------------
"""
from django.contrib import admin
from kitchensink.device.models import Make, Device


class MakeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Make)
admin.site.register(Device)
