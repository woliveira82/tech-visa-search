from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('techvisa.urls')),
    path('companies', include('techvisa.urls')),
    path('admin/', admin.site.urls),
]
