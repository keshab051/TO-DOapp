from django.contrib import admin
from .models import Task
 
#admin pannel costumize
class Taskadmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')

# Register your models here.
admin.site.register(Task,Taskadmin)