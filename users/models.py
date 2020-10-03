from django.db import models
#from phone_field import PhoneField

class Userinfo(models.Model):

    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    address = models.CharField(max_length=20) # might verify these in future
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=12)
    zipcode = models.IntegerField(null = True)  #
    dob = models.CharField(max_length=20)       #
    phone = models.CharField(null = True, max_length=20)   #
    email = models.EmailField(max_length=20)

    def __str__(self): #string representation in db
        return self.fname + ' ' + self.lname
