from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# این روتر (Router) خودش به صورت اتوماتیک لینک‌ها رو برامون می‌سازه
router = DefaultRouter()
router.register(r'genres', views.GenreViewSet)
router.register(r'studios', views.StudioViewSet)
router.register(r'animes', views.AnimeViewSet)
router.register(r'user-list', views.UserAnimeListViewSet, basename='user-list')

urlpatterns = [
    path('', include(router.urls)),
]