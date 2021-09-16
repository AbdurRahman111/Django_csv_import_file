from django.contrib import admin
from .models import name_database
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class Bran(ImportExportModelAdmin):
    pass

admin.site.register(name_database, Bran)
