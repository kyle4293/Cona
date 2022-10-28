from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Assignment, AssignmentAdmin)