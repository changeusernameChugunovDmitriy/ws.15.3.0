from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, \
    CreateAPIView

from .models import Film
from .serializers import FilmSerializer


class FilmGetList(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmCreate(CreateAPIView):
    queryset = Film
    serializer_class = FilmSerializer


