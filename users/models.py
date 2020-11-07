from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
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
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default=None)

    def __str__(self): #string representation in db
        return self.fname + ' ' + self.lname

   # def get_absolute_url(self):
    #    return reverse('user-list', kwargs={'pk': self.pk})


class transactions(models.Model):
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default=None)
    # account_id
    amount = models.CharField(max_length=20)
    tname = models.CharField(max_length=20) #decimal field
    recipient = models.CharField(max_length=20)
    date = models.DateField(max_length=20)


    def __str__(self): #string representation in db
        return self.tname + ' ' + self.amount

    #def get_absolute_url(self):
     #   return reverse('taction-list', kwargs={'pk': self.pk})



class bills(models.Model):
    bname = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default=None)
    #bamount = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    bamount = models.CharField(max_length=20)
    duedate = models.DateField(max_length=20)

    def __str__(self): #string representation in db
        return self.bname + ' ' + self.bamount

   # def get_absolute_url(self):
    #    return reverse('bills-list', kwargs={'pk': self.pk})



# class accounts(models.Model):