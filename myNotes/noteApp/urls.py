from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name="notes"),
    path('settings/', views.settings, name="settings"),
    path('notes/', views.notes, name="notes"),
    path('editNote/<str:pk_note>/', views.editNote, name="editNote"),
    path('deleteNote/<str:pk_delete>/', views.deleteNote, name="deleteNote"),
    path('createNote', views.createNote, name="createNote"),
    path('login/', views.loginPage, name="loginPage"),
    path('register/', views.registerPage, name="registerPage"),
    path('logout/', views.logoutPage, name="logoutPage"),
]