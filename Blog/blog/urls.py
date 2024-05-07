from django.urls import path
from . import views


urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("posts/<int:pk>/", views.blog_detail, name="blog_details"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]

