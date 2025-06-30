from django.urls import path
from . import views
urlpatterns = [
    path('/addtask/',views.AddTask,name='AddTask'),
    path('/mark_as_done/<int:pk>',views.mark_as_done,name='mark_as_done'),
    path('/mark_as_undo/<int:pk>',views.mark_as_undo,name='mark_as_undo'),
]