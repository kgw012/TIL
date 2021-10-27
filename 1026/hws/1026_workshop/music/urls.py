from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artists_list_create),
    path('artists/<int:artist_pk>/', views.artists_get),
    path('artists/<int:artist_pk>/music/', views.music_create),
    path('music/', views.music_list),
    path('music/<int:music_pk>/', views.music_get_update_delete),
]
