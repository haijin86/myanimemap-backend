from django.contrib import admin
from .models import Genre, Studio, Anime

# اضافه کردن مدل‌ها به پنل ادمین
admin.site.register(Genre)
admin.site.register(Studio)

# یه کم شخصی‌سازی برای جدول انیمه تا قشنگ‌تر نمایش داده بشه
@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_fa', 'episodes', 'status') # ستون‌هایی که تو لیست میاره
    list_filter = ('status',) # فیلتر سمت راست صفحه
    search_fields = ('title_en', 'title_fa') # باکس جستجو