from django.contrib import admin

# Register your models here.

from .models import Board
from import_export.admin import ImportExportModelAdmin
@admin.register(Board)
class ViewAdmin(ImportExportModelAdmin):
	pass