from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='movies/index'),
        path('<int:movie_id>', views.detail, name='movies/detail')
]
