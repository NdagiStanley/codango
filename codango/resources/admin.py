from django.contrib import admin
from models import Resources

# Register your models here.

class ResourcesAdmin(admin.modelAdmin):
	pass

admin.site.register(Resources, ResourcesAdmin)