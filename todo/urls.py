from django.urls import path
from todo import views

urlpatterns = [
    path('addtask/', views.addtask, name = 'addtask'),
    path('mark_as_done/<int:pk> ', views.mark_as_done, name = 'mark_as_done'),
    path('mark_as_undone/<int:pk> ', views.mark_as_undone, name = 'mark_as_undone'),
    path('delete/<int:pk> ', views.delete, name = 'delete'),
    path('delete_completed_task/<int:pk> ', views.delete_completed_task, name = 'delete_completed_task'),
    path('updated/<int:pk> ', views.updated, name = 'updated'),
    
]