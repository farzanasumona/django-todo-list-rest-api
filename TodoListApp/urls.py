from django.urls import path

from TodoListApp import views
from TodoListApp.views import todo_task_create, todo, TodoSearch

urlpatterns = [
    path('create/', todo_task_create, name='create-task'),
    path('<int:pk>', todo, name='get_by_id_task'),
    path('all/', TodoSearch.as_view())

]
