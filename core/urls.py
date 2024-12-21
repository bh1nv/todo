from django.urls import path
from core import views

urlpatterns = [
    path("",views.home, name="task_list"),
    path("create", views.task_create, name="task_create"),
    path("<int:task_pk>", views.task_detail, name="task_detail"),
    path("<int:task_pk>/update", views.task_update, name="task_update"),
    path("<int:task_pk>/delete", views.task_delete, name="task_delete"),
]