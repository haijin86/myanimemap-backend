from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # این خط رو اضافه کردیم تا لینک‌های API کار کنن
    path('api/', include('anime.urls')), 
]