from django.contrib import admin
from hierarchyapp.models import Information
from mptt.admin import MPTTModelAdmin

admin.site.register(Information, MPTTModelAdmin)
