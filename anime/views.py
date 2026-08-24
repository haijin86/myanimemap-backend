from rest_framework import viewsets
from .models import Genre, Studio, Anime, UserAnimeList
from .serializers import GenreSerializer, StudioSerializer, AnimeSerializer, UserAnimeListSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    
class UserAnimeListViewSet(viewsets.ModelViewSet):
    queryset = UserAnimeList.objects.all()
    serializer_class = UserAnimeListSerializer