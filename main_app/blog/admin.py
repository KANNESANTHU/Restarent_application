from django.contrib import admin
from .models import Categery,Post,Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
admin.site.register(Post)
admin.site.register(Categery)
admin.site.register(Comment)