from django.contrib import admin
from models import Resource

# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
	pass

admin.site.register(Resource, ResourceAdmin)