from django.db import models

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
