from . import views
from django.urls import path

app_name = "talk"

urlpatterns = [
    path('index', views.index, name="index"),
    path('delete', views.delete, name="delete"),
    path('american', views.american, name="american"),
    path('samurai', views.samurai, name="samurai"),
]
