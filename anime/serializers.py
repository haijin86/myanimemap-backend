from rest_framework import serializers
from .models import Genre, Studio, Anime, UserAnimeList

# مترجم ژانرها
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'  # یعنی تمام فیلدهای این جدول رو ترجمه کن

# مترجم استودیوها
class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

# مترجم اصلی انیمه‌ها
class AnimeSerializer(serializers.ModelSerializer):
    # چون ژانر و استودیو جداول جداگانه‌ای هستن، اینجا بهش میگیم از مترجم‌های اونا استفاده کن
    genres = GenreSerializer(many=True, read_only=True)
    studios = StudioSerializer(many=True, read_only=True)

    class Meta:
        model = Anime
        fields = '__all__'
        
        
        
# مترجم لیست انیمه‌های کاربر
class UserAnimeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnimeList
        fields = '__all__'