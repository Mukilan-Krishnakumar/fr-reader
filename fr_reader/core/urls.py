from django.urls import path
from core import views


urlpatterns = [
    path("", views.translate_site, name="translate_site"),
    path("health", views.health, name="health"),
]
