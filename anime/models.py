from django.db import models
from django.contrib.auth.models import User
# ۱. جدول ژانرها


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام ژانر (مثل اکشن)")

    def __str__(self):
        return self.name

# ۲. جدول استودیوها


class Studio(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="نام استودیو (مثل MAPPA)")

    def __str__(self):
        return self.name

# ۳. جدول اصلی انیمه‌ها


class Anime(models.Model):
    # وضعیت‌های پخش
    STATUS_CHOICES = (
        ('airing', 'در حال پخش'),
        ('finished', 'پایان یافته'),
        ('upcoming', 'به زودی'),
    )
    cover_image = models.ImageField(upload_to='anime_covers/', null=True, blank=True, verbose_name="عکس کاور انیمه")
    title_en = models.CharField(max_length=255, verbose_name="عنوان انگلیسی")
    title_fa = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="عنوان فارسی")
    synopsis = models.TextField(verbose_name="خلاصه داستان")
    episodes = models.IntegerField(default=0, verbose_name="تعداد قسمت‌ها")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='finished', verbose_name="وضعیت پخش")

    # روابط (یک انیمه میتونه چند ژانر و چند استودیو داشته باشه)
    genres = models.ManyToManyField(Genre, verbose_name="ژانرها")
    studios = models.ManyToManyField(Studio, verbose_name="استودیوها")

    def __str__(self):
        return self.title_en




# ۴. جدول لیست شخصی کاربران (قلب MyAnimeMap)
class UserAnimeList(models.Model):
    LIST_STATUS_CHOICES = (
        ('watching', 'در حال تماشا'),
        ('completed', 'کامل شده'),
        ('on_hold', 'متوقف شده (On Hold)'),
        ('dropped', 'رها شده (Dropped)'),
        ('plan_to_watch', 'قصد تماشا دارم'),
    )

    # ارتباط با جدول کاربرها و جدول انیمه‌ها
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name="انیمه")
    
    # اطلاعات لیست
    status = models.CharField(max_length=20, choices=LIST_STATUS_CHOICES, default='plan_to_watch', verbose_name="وضعیت")
    score = models.IntegerField(default=0, verbose_name="امتیاز (۱ تا ۱۰)")
    episodes_watched = models.IntegerField(default=0, verbose_name="تعداد قسمت‌های دیده شده")

    class Meta:
        # این خط میگه یه کاربر نمیتونه یه انیمه رو دو بار به لیستش اضافه کنه!
        unique_together = ('user', 'anime')
        verbose_name = "لیست انیمه کاربر"
        verbose_name_plural = "لیست انیمه کاربران"

    def __str__(self):
        return f"{self.user.username} - {self.anime.title_en}"