from django.contrib import admin
from .models import Books, Comment

admin.site.register(Books)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'book', 'datetime_created']
