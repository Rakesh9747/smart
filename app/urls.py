from django.urls import path, include
from . import views
from .views import search_institution

urlpatterns = [
    path("", search_institution),
    path("autosuggest/", views.autosuggest, name="autosuggest"),
]
