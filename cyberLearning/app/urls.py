from django.urls import path
from .views import (
    home,
    edit_json,
    select_role,
    set_role,
    student_view,
    teacher_view,
    admin_view,
    render_module,  # Add this import
)

urlpatterns = [
    path("", home, name="home"),
    path("select-role/", select_role, name="select_role"),
    path("set-role/<str:role>/", set_role, name="set_role"),
    path("module/", render_module, name="render_module"),  # Add this route
    path("module/edit/", edit_json, name="edit_json"),  # Add this route
    path("student/", student_view, name="student_view"),
    path("teacher/", teacher_view, name="teacher_view"),
    path("admin/", admin_view, name="admin_view"),
]
