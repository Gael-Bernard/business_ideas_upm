from django.urls import include, path

from . import views


app_name = "ideas"

urlpatterns = [
    path("", views.list, name="index"),
    path("list", views.list, name="list"),
    path("idea/<int:idea_id>", views.idea, name="idea")
]