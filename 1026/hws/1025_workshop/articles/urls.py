from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_create),
    path('<int:article_pk>/', views.get_update_delete),
]
