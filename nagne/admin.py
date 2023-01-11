from django.contrib import admin
from .models import Post, StudyGroup

class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Post, PostAdmin)

class StudyGroupAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(StudyGroup, StudyGroupAdmin)