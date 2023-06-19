from . import views
from django.urls import path

app_name = "talk"

urlpatterns = [
    path('index', views.index, name="index"),
]
