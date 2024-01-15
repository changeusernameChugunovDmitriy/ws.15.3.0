from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductGet.as_view()),
    path('create', ProductPost.as_view()),
    path('update/<int:pk>', ProductUpdate.as_view()),
    path('delete/<int:pk>', ProductDelete.as_view()),
]