from django.urls import path

from . import views

app_name = "firstapp"


urlpatterns = [
    path("", views.index, name="index"),
    path("poop/", views.poop, name="poo"),
    path("item/", views.item_view, name="item_url_name")
] 