from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', name="homepage")
    path('users/', include('users.urls')),
    path('users/register/', include('users.urls')),
    path('users/login/', include('users.urls')),
    path('users/signup/', include('users.urls')),
]
