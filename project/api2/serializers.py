from rest_framework import serializers

from .models import Film, Director, Genre


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['fio', 'year']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']
class FilmSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genre = GenreSerializer()

    class Meta:
        model = Film
        fields = ["title", "year_release", "country", "director", "genre"]

    def create(self, validated_data):
        director_data = validated_data.pop('director')
        genre_data = validated_data.pop('genre')

        director_instance, _ = Director.objects.get_or_create(**director_data)
        genre_instance, _ = Genre.objects.get_or_create(**genre_data)

        film = Film.objects.create(director=director_instance, genre=genre_instance, **validated_data)
        return film