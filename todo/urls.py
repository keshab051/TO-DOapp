from django.urls import path
from . import views
urlpatterns = [
    path('/addtask/',views.AddTask,name='AddTask'),
    path('/updatetask/',views.updatetask,name='updatetask'),
    path('/completedtask/',views.completedtask,name='completedtaks'),
]