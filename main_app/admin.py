from django.contrib import admin

from main_app.models import Theatre

@admin.register(Theatre)
class Theatreadmin(admin.ModelAdmin):
    pass

