from django.db import models

class EmpLogin(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    class Meta:
        db_table="EmpLogin"

class UsersCustomer(models.Model):  
    name = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)
    cust_email_verified = models.CharField(max_length=50,blank=True, null=True)
    class Meta:
        db_table="UsersCustomer"


class BookMechanic(models.Model):
    issueid = models.CharField(max_length=1000,blank=True, null=True)
    address = models.CharField(max_length=500,blank=True, null=True)
    zipcode = models.CharField(max_length=100,blank=True, null=True)
    vehicleType = models.CharField(max_length=100,blank=True, null=True)
    vehicleNo = models.CharField(max_length=100,blank=True, null=True)
    issuedesc = models.CharField(max_length=500,blank=True, null=True)
    phone = models.CharField(max_length=500,blank=True, null=True)
    lat = models.CharField(max_length=200,blank=True, null=True)
    lng = models.CharField(max_length=200,blank=True, null=True)
    class Meta:
        db_table="BookMechanic"

class UsersCurrentAddress(models.Model):
    issueid = models.CharField(max_length=1000,blank=True, null=True)
    address = models.CharField(max_length=500,blank=True, null=True)
    zipcode = models.CharField(max_length=100,blank=True, null=True)
    vehicleType = models.CharField(max_length=100,blank=True, null=True)
    vehicleNo = models.CharField(max_length=100,blank=True, null=True)
    issuedesc = models.CharField(max_length=500,blank=True, null=True)
    issuetype = models.CharField(max_length=500,blank=True, null=True)
    phone = models.CharField(max_length=500,blank=True, null=True)
    lat = models.CharField(max_length=200,blank=True, null=True)
    lng = models.CharField(max_length=200,blank=True, null=True)
    username = models.CharField(max_length=100)
    issue_status_id = models.CharField(max_length=69,blank=True, null=True)
    
    class Meta:
        db_table="UsersCurrentAddress"

class Feedback(models.Model):
    issueid = models.CharField(max_length=1000,blank=True, null=True)
    desc = models.CharField(max_length=5000,blank=True, null=True)
    
    cust_name = models.CharField(max_length=500,blank=True, null=True)
    cust_username = models.CharField(max_length=500,blank=True, null=True)
    mech_name = models.CharField(max_length=500,blank=True, null=True)
    mech_username = models.CharField(max_length=500,blank=True, null=True)
    RATING_CHOICES = (
        (1, 'Poor'),
        (2, 'Below Average'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    )

    rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    issue_description = models.TextField(max_length=5000,blank=True, null=True)
    class Meta:
        db_table="Feedback"

class Profile(models.Model):
    phone = models.CharField(max_length=1000,blank=True, null=True)
    no_of_bookings = models.CharField(max_length=5000,blank=True, null=True)
    rating = models.CharField(max_length=200,blank=True, null=True)
    cust_name = models.CharField(max_length=500,blank=True, null=True)
    cust_username = models.CharField(max_length=500,blank=True, null=True)
    class Meta:
        db_table="Profile"

class Bookings(models.Model):
    cust_username =models.CharField(max_length=500,blank=True, null=True)   
    mech_name= models.CharField(max_length=200,blank=True, null=True)
    booking_date = models.CharField(max_length=200,blank=True, null=True)
    booking_time = models.CharField(max_length=200,blank=True, null=True)
    issue_desc = models.CharField(max_length=2000,blank=True, null=True)
    issue_resolved_status =models.CharField(max_length=200,blank=True, null=True)
    mech_mobile = models.CharField(max_length=200,blank=True, null=True)
    class Meta:
        db_table="Bookings"

# class ongoing_bookings_customer(models.Model):
#     mech_username = models.CharField(max_length=500,blank=True, null=True)
#     issueid = models.CharField(max_length=1000,blank=True, null=True) 




