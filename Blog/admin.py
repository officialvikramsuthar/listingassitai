from django.contrib import admin
from .models import Blog, Tag

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
