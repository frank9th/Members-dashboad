from django.contrib import admin
from .models import Leader
from .models import Members 

# Register your models here.
admin.site.register(Leader)
admin.site.register(Members)
