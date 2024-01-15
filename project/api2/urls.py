from django.urls import path

from .views import *

urlpatterns = [
    path('', FilmGetList.as_view()),
    path('rud/<int:pk>', FilmUpdateDelete.as_view()),
    path('create', FilmCreate.as_view())

]