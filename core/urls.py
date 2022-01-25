from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('customUser.urls')),
    path('auction/', include('auction.urls')),
]
