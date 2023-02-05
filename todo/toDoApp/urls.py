from django.urls import path
from toDoApp.views import index, new_task, switch, rem_task

urlpatterns = [
    path('', index, name='Home'),
    path('new_task/', new_task, name='new_task'),
    path('switch/<int:task_id>/', switch, name='switch'),
    path('rem_task/<int:task_id>/', rem_task, name='rem_task')
]

