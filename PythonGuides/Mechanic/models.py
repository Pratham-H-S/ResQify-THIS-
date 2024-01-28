from django.db import models

# Create your models here.


class UsersMechanic(models.Model):
    name = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)
    class Meta:
        db_table="UsersMechanic"

class MechanicDetails(models.Model):
    mech_Address = models.CharField(max_length=500)
    mech_city = models.CharField(max_length=50)
    mech_zipcode = models.CharField(max_length=30)
    mech_shop = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    lat = models.CharField(max_length=200,blank=True, null=True)
    lng = models.CharField(max_length=200,blank=True, null=True)
    class Meta:
        db_table="MechanicDetails"

class Booking_status(models.Model):
    issueid = models.CharField(max_length=1000,blank=True, null=True)
    cust_name = models.CharField(max_length=500,blank=True, null=True)
    cust_username = models.CharField(max_length=500,blank=True, null=True)
    mech_name = models.CharField(max_length=500,blank=True, null=True)
    mech_username = models.CharField(max_length=500,blank=True, null=True)
    mech_assigned = models.CharField(max_length=50,blank=True, null=True)
    issue_resolved_status  = models.CharField(max_length=50,blank=True, null=True)
    cust_lat = models.CharField(max_length=200,blank=True, null=True)
    cust_lng =models.CharField(max_length=200,blank=True, null=True)
    mech_lat = models.CharField(max_length=200,blank=True, null=True)
    mech_lng = models.CharField(max_length=200,blank=True, null=True)
    duration_seconds =  models.CharField(max_length=50,blank=True, null=True)
    duration_kilometers =  models.CharField(max_length=50,blank=True, null=True)
    booking_time =  models.CharField(max_length=200,blank=True, null=True)
    booking_date =  models.CharField(max_length=200,blank=True, null=True)
    class Meta:
        db_table="Booking_status"

