from django.urls import path, include
from . import views
from .views import search_institution

urlpatterns = [
    path("", search_institution),
    path("autosuggest/", views.autosuggest, name="autosuggest"),
     path("search/", views.search_institution, name="search"),
     path("students/", views.view_students, name="view_students"), 
         path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-students/", views.admin_students, name="admin_students"),
    path("admin-logout/", views.admin_logout, name="admin_logout"),
    path("download-report/", views.download_students_report, name="download_report"),

    path("apply/<int:inst_id>/", views.apply_student, name="apply_student"),
]
