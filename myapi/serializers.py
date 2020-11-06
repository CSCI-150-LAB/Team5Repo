from rest_framework import serializers
from users.models import bills, Userinfo

class billsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bills
        fields = ('bname', 'bamount', 'duedate', 'user_id')


class UserinfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userinfo
        fields = ('fname', 'lname', 'address', 'city', 'state', 'zipcode', 'dob', 'phone', 'email', 'author')