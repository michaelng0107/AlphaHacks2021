from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
]

urlpatterns += [
    path('login/', include('rest_framework.urls')),
]