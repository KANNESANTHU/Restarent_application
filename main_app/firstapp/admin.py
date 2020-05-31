from django.contrib import admin
from .models import Register,Categery,Meal
from django_summernote.admin import SummernoteModelAdmin

class MealAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Register)

admin.site.register(Categery)
admin.site.register(Meal)
