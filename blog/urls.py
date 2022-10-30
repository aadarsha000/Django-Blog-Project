from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",views.postlist, name="home"),
    path("detail/<int:id>/", views.postdetail, name="postdetail"),
    path("create/", views.postCreate, name="postcreate"),
]

