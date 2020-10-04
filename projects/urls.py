from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home name='home'),
    path('users/', include('users.urls')),
    path('users/register/', include('users.urls')),
    path('users/login/', include('users.urls')),
    path('users/signup/', include('users.urls')),
]