from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("notes/<str:userid>", views.notes, name="notes"),
    path("create", views.create, name="create"),
    path("new/<path:videoid>", views.newnote, name="newnote"),
    path("note/<int:id>", views.note_view, name="note"),
    path("subject/<str:subj>", views.subject_view, name="subject"),
    path("note/edit/<str:title>", views.edit_note, name="edit"),
    path("note/delete/<str:title>", views.delete_note, name="delete"),
    path("calendar", views.calendar_view, name="calendar"),
    path("calendar/delete/<str:subject>", views.delete_event, name="deletevent"),
]