from rest_framework import serializers
from .models import Genre, Studio, Anime, UserAnimeList
from django.contrib.auth.models import User
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
        read_only_fields = ('user',)
        
        
        
# مترجم ثبت‌نام کاربر جدید
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # این خط میگه پسورد رو فقط بگیر ولی هیچوقت به کسی نشونش نده
        extra_kwargs = {'password': {'write_only': True}} 

    # این تابع پسورد رو قبل از ذخیره شدن، قفل (رمزنگاری) می‌کنه
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user