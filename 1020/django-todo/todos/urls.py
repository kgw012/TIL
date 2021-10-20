from django.urls import path
from . import views

app_name="todos"
urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]