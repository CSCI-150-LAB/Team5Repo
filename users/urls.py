from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_, name='login'),
    path('signup/', views.signup_, name='signup'),
    path('landing/', views.landingpage, name='landing'),
    path('logout/', views.logout_, name='logout'),
]
