from django.urls import path
from . import views

urlpatterns = [
    path("api/about/", views.about),
    path("api/skills/", views.skills),
    path("api/projects/", views.projects),
    path("api/resume/", views.resume),
    path("api/random-fact/", views.random_fact),
    path("api/hireme/", views.hireme),
]
