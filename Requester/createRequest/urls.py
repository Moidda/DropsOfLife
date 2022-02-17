from django.urls import path
from . import views


app_name = 'createRequest'
urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.processRequest, name='processRequest'),
]