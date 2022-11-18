from django.urls import include, path

from . import views


app_name = "ideas"

urlpatterns = [
    path("", views.list, name="index"),
    path("list", views.list, name="list"),
    path("idea/<int:idea_id>", views.idea, name="idea"),
    path("idea_new", views.idea_new, name="idea_new"),
    path("idea_new_post", views.idea_new_post, name="idea_new_POST")
]