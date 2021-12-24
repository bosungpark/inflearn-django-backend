from django.contrib import admin
from .models import myText, Comment

class myTextAdmin(admin.ModelAdmin):
    list_display=('pk','title')

class CommentAdmin(admin.ModelAdmin):
    list_display=('pk','comment')

admin.site.register(myText,myTextAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
