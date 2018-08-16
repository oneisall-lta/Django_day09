from django.urls import path

from homeworkapp import views

app_name = 'homework'

urlpatterns = [
    path('gostudent/', views.gostudent),
    path('showall/', views.getallstudents, name='all'),
]
