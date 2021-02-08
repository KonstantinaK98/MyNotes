from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.notes, name="notes"),
    path('/', views.notes, name="notes"),
    path('settings/', views.settings, name="settings"),
    path('notes/', views.notes, name="notes"),
    path('editNote/<str:pk_note>/', views.editNote, name="editNote"),
    path('deleteNote/<str:pk_delete>/', views.deleteNote, name="deleteNote"),
    path('createNote', views.createNote, name="createNote"),
    path('login/', views.loginPage, name="loginPage"),
    path('register/', views.registerPage, name="registerPage"),
    path('logout/', views.logoutPage, name="logoutPage"),
    url('change_password/', views.change_password, name='change_password'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))
]