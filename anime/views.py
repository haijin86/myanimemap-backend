from rest_framework import viewsets
from .models import Genre, Studio, Anime, UserAnimeList
from .serializers import GenreSerializer, StudioSerializer, AnimeSerializer, UserAnimeListSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    # این فیلترها مال اینجاست:
    filterset_fields = ['status', 'genres', 'studios'] 
    search_fields = ['title_en', 'title_fa', 'synopsis'] 
    ordering_fields = ['episodes', 'id']
    
class UserAnimeListViewSet(viewsets.ModelViewSet):
    serializer_class = UserAnimeListSerializer
    permission_classes = [IsAuthenticated] 
    
    # فیلترها مخصوص لیست شخصی:
    filterset_fields = ['status', 'score'] # فیلتر بر اساس در حال تماشا بودن یا نمره دادن
    search_fields = ['anime__title_en', 'anime__title_fa'] # سرچ تو اسم انیمه موجود در لیست
    ordering_fields = ['score', 'episodes_watched']

    def get_queryset(self):
        return UserAnimeList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        



# منطق ثبت نام کاربر
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # یعنی همه (حتی کاربرانی که لاگین نیستن) بتونن این فرم رو ببینن
    serializer_class = RegisterSerializer 
        
