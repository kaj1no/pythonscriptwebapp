from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.run,name='remder'),
    path('fileupload',views.fileup,name='fileupload'),
    path('download',views.downl,name='download'),
    path('scriptrun',views.script,name='script'),
]