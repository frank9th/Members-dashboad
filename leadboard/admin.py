from django.contrib import admin
from .models import Leader
from .models import Members 
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Leader)
@admin.register(Members)
class ViewAdmin(ImportExportModelAdmin):
	pass
