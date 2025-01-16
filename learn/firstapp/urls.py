from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("poop", views.poop, name="what does this do")
] 