from django.contrib import admin

from lab_3.models import Theatre

@admin.register(Theatre)
class Theatreadmin(admin.ModelAdmin):
    pass

