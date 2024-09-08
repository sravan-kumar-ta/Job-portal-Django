from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('account.urls')),
    path('api/company/', include('company.urls')),
    path('api/admin/', include('admin.urls')),
]
