from django.contrib import admin
from .models import Genre, Studio, Anime
from .models import Genre, Studio, Anime, UserAnimeList
# اضافه کردن مدل‌ها به پنل ادمین
admin.site.register(Genre)
admin.site.register(Studio)

# یه کم شخصی‌سازی برای جدول انیمه تا قشنگ‌تر نمایش داده بشه
@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_fa', 'episodes', 'status') # ستون‌هایی که تو لیست میاره
    list_filter = ('status',) # فیلتر سمت راست صفحه
    search_fields = ('title_en', 'title_fa') # باکس جستجو
    
    
    
    

@admin.register(UserAnimeList)
class UserAnimeListAdmin(admin.ModelAdmin):
    list_display = ('user', 'anime', 'status', 'score', 'episodes_watched')
    list_filter = ('status', 'score')
    search_fields = ('user__username', 'anime__title_en')