from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'bills', views.billsViewSet)
router.register(r'Userinfo', views.UserinfoViewSet)

urlpatterns = [
    path('', include(router.urls)), #possibly rest/
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]