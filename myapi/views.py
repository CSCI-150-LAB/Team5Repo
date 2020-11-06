from django.shortcuts import render
from rest_framework import viewsets

from .serializers import billsSerializer, UserinfoSerializer
from users.models import bills, Userinfo

class billsViewSet(viewsets.ModelViewSet): #handles get/post
    queryset = bills.objects.all().order_by('bname')
    serializer_class = billsSerializer



class UserinfoViewSet(viewsets.ModelViewSet): #handles get/post
    queryset = Userinfo.objects.all().order_by('fname')
    serializer_class = UserinfoSerializer