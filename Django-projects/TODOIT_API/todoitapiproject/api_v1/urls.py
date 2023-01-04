from django.urls import path
from tasks import views as tasks_views


urlpatterns = [
    # tasks
    path('tasks/', tasks_views.get_tasks_list),
    path('tasks/task/<int:id>', tasks_views.get_or_update_task_by_id),
    path('tasks/priorities', tasks_views.get_tasks_by_priority),
    path('tasks/complete_all_task', tasks_views.complete_all_task),
    path('tasks/uncomplete_all_task', tasks_views.uncomplete_all_task),
    path('tasks/delete_all_tasks', tasks_views.delete_all_tasks),
]
