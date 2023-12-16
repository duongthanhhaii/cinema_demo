from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),

    path('film', views.MovieView.as_view(), name = 'film'),
    path('add_film', views.add_film),
    path('update_film/<str:id>', views.update_film),
    path('delete_film/<str:id>', views.delete_film),

    path('schedule', views.schedule),
    path('ticket', views.ticket),

    path('get_film', views.api_get_movies),
    path('post_film', views.api_post_movie),
    path('update_film/<str:id>', views.api_update_movie),
    path('delete_film/<str:id>', views.api_delete_movie),

]