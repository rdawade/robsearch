from django.http.response import HttpResponse
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.function,name='projects'),
    path('project/<str:pk>/',views.projec,name="pro"),
    path('create-project/',views.createproject,name="create-project"),
    path('update-project/<str:pk>/',views.updateproject,name="update-project"),
    path('delete-project/<str:pk>/',views.deleteproject,name="delete-project")
]
