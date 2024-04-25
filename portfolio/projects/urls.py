from django.urls import path
from projects import views

urlpatterns = [
    path("projects/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]

