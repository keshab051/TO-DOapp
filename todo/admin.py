from django.contrib import admin
from .models import Task
 
#admin pannel customize 
class Taskadmin(admin.ModelAdmin):
    #these are the inbuilt attribute to customize admin pannel
    list_display = ('task','is_completed','updated_at')
    search_fields = ('task',)

# Register your models here.
admin.site.register(Task,Taskadmin)