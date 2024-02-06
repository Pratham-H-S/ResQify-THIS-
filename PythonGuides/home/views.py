from django.shortcuts import render,redirect
from django.http import HttpResponse
from requests import session
from. models import *
from Mechanic.models import *
from home.encrypt_util import *
import googlemaps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.core.mail import send_mail
from PythonGuides.settings import EMAIL_HOST_USER
import os
def navbar(request):
    if request.method == 'POST':
        username = (request.session['cust_username'])
        print(username)
        # udata = UsersCurrentAddress.objects.get(username = username)
        key = settings.GOOGLE_API_KEY
            # eligable_locations = Locations.objects.filter(place_id__isnull=False)
        if UsersCustomer.objects.filter(username =username).exists():
            udata = UsersCurrentAddress.objects.get(username = username)
            locations = []
            latitude = udata.lat
            longitude = udata.lng
            gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
            result = gmaps.reverse_geocode((latitude, longitude))
            address = result[0]['formatted_address']
            # zipcode = result[0]['postal_code']
            udata.address= address
            # udata.zipcode = zipcode
            udata.save()
            print(result)
        for a in range(0,1): 
            data = {
                    "lat":float(latitude), 
                    "lng": float(longitude), 
                    "name":'',  
                }

            locations.append(data)

            print(locations)
            instance_ip_or_domain = '127.0.0.1'
        context = {
            "key": key, 
           "locations": locations,
            "address" : address,
            'instance_ip_or_domain':instance_ip_or_domain
            
             
            }
            
        return render(request, 'customer_map.html', context=context)

    return render(request, 'loading_bar.html')




def signup(request):
    if  request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        print(name)
        if (password1 == password2):
            encryptpass= encrypt(password1)
            if UsersCustomer.objects.filter(username =username).exists():
                
                return HttpResponse('User already exits')
            else:
                data = UsersCustomer(name=name,username=username,email=email,mobile=phone,password= encryptpass,cust_email_verified = '0')
                data.save()
                ldata = UsersCurrentAddress(username=username)
                ldata.save()
                issue = Booking_status(cust_username=username)
                issue.save()
                profil = Profile(cust_username=username,rating = 5,phone=phone,no_of_bookings = 0,cust_name = name)
                profil.save()
                request.session['cust_username'] = username
                return redirect('otp')
        else:
            return render(request, 'login_final.html')
  
    return render(request, 'login_final.html')


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        p1 = request.POST.get('p1', '')
        p2 = request.POST.get('p2', '')
        if(p1 == p2):
            request.session['cust_username'] = username
            request.session['newp'] = p1
            return redirect ('otp_forgot_passwd')
    return render(request, 'forgot_password.html')  


global num
num = 0
def otp_forgot_passwd(request):
    global num
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')

        entered_otp = f"{otp1}{otp2}{otp3}{otp4}"
        if (int(entered_otp) == int(num)):
            dat = UsersCustomer.objects.get(username = request.session['cust_username'])
            encryptpass= encrypt(request.session['newp'])
            dat.password = encryptpass
            dat.save()
            messages.success(request, 'OTP verified successfully!')
            return redirect('login')
        else:
            messages.success(request, 'OTP not verified successfully!')
            return HttpResponse('invalid Otp')
    else:
        mail = UsersCustomer.objects.get(username = request.session['cust_username'])
        num = random.randrange(1000,9999)
        subject = ''' Hello,
 
{} is your one-time passcode (OTP) for the ResQify app.
 
Use this OTP to reset your password.
 
The code was requested from the ResQify's App on google your device.It will be valid for 4 hours.
 
 
Enjoy the app!
 
ResQify's team'''
        send_mail('Your One Time Passcode for ResQify',subject.format(num),EMAIL_HOST_USER,[mail.email],fail_silently=True)
        return  render(request,"forgot_passwrd_otp.html")
            


def login(request):
    if request.method == "POST":
        username = request.POST['username'] 
        try:
            verify = UsersCustomer.objects.get(username = username,cust_email_verified = '1')
            password = request.POST['password']
            print(verify.username)
            decrypted = decrypt(verify.password)
            
            if(decrypted == password):
                request.session['cust_name'] = verify.name
                request.session['cust_username'] = verify.username
                instance_ip_or_domain = '127.0.0.1'
                context = {'instance_ip_or_domain':instance_ip_or_domain}
                return render(request,'accept_rules.html',context= context)
            else:
                return JsonResponse({'error': 'Invalid username or password'})
        except:
            return JsonResponse({'error': 'Invalid username or password'})
        # if (verify == username):
        #     print(username)
        
    return render(request,"loginSignup.html")

def logout_cust(request):
    if 'cust_username' in request.session:
        del request.session['cust_username']
        
    if 'cust_name' in request.session:
        del request.session['cust_name']
    
    # You can perform additional logout actions here if needed

    return redirect('home_page')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # This is used to exempt the view from CSRF protection. Use it cautiously.
def save_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            lat = request.COOKIES.get("lat")
            long = request.COOKIES.get("long")
            print(latitude)
            print(longitude)
            print("post req ")
            username = (request.session['cust_username'])
            print("save location call")
            # idata = UsersCurrentAddress(username=username,lat = latitude,lng = longitude)
            # idata.save()
            udata = UsersCurrentAddress.objects.get(username = username)
            udata.lat = latitude
            udata.lng = longitude
            print(latitude)
            udata.save()
            # if (UsersCustomer.objects.filter(username =username).exists() == True):
      
    
            key = settings.GOOGLE_API_KEY
            # eligable_locations = Locations.objects.filter(place_id__isnull=False)
            locations = []
            print("Called from login")
            for a in range(0,1): 
                data = {
                    "lat":float(latitude), 
                    "lng": float(longitude), 
                    "name":'',
                    
                }

                locations.append(data)
            instance_ip_or_domain = '127.0.0.1'
            print(locations)
            context = {
                "key": key, 
                "locations": locations,
                'instance_ip_or_domain': instance_ip_or_domain
            }
            
            return render(request, 'customer_map.html', context)


            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return render(request,"location.html")


def BookMechanic(request):
    if request.method == 'POST':
        username = request.session['cust_username']
        Address = request.POST['Address']
        City = request.POST['City']
        ZipCode = request.POST['ZipCode']
        print(Address)
        adress_string = str(Address)+", "+str(ZipCode)+", "+str(City)+", "+"India"

        gmaps = googlemaps.Client(key = settings.GOOGLE_API_KEY)
        result = gmaps.geocode(adress_string)[0]    
        lat = result.get('geometry', {}).get('location', {}).get('lat', None)
        lng = result.get('geometry', {}).get('location', {}).get('lng', None)
        print(lat)
        print(lng)
        udata = UsersCurrentAddress.objects.get(username = username)
        udata.lat = lat
        udata.lng = lng

        return render(request,"issue_detailpage.html") 
        # Address = request.POST['Address']
        # City = request.POST['City']
        # ZipCode = request.POST['ZipCode']
        # print(Address)
        # adress_string = str(Address)+", "+str(ZipCode)+", "+str(City)+", "+"India"

        # gmaps = googlemaps.Client(key = settings.GOOGLE_API_KEY)
        # result = gmaps.geocode(adress_string)[0]    
        # lat = result.get('geometry', {}).get('location', {}).get('lat', None)
        # lng = result.get('geometry', {}).get('location', {}).get('lng', None)
        # # print(lat)
        # # print(lng)F
        # # return HttpResponse("success")
        # gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        # result = gmaps.reverse_geocode((lat, lng))

        # if result:
        #         # Assuming the first result is the most relevant one
        #     address = result[0]['formatted_address']

        #     print(f"Address: {address}")
        #     return HttpResponse(address)
        # else:
        #     print("Reverse geocoding API did not return any results.")
        #     return HttpResponse("No address found")

def loc(request):
    return render(request,"forgotpass.html") 

import random

# Generate a random integer between a specified range

def vehicle_details(request):
    if request.method == 'POST':
        username = request.session['cust_username']
        print(username)
        vehicleType = request.POST['vehicleType']
        issuetype = request.POST['issueType']
        vehicleNumber = request.POST['vehicleNumber']
        issueDescription = request.POST['issueDescription']
        
        Major_issues =  ['Break Failure','Engine Overheating','Fluid Leaks','Smoke or Burning Smells']
        Minor_issues = ['Strange Noises','Fuel System Problems','Tire Issues']
        low_priority = ['Maintenance Reminders','Accessory Malfunctions']
        for i in Major_issues:
            if i == issuetype:
                issuetype= 'major'
        for i in Minor_issues:
            if i == issuetype:
                issuetype= 'minor'
        for i in low_priority:
            if i == issuetype:
                issuetype= 'low'
        mobileNumber = request.POST['mobileNumber']
        issueId = random.randint(1, 1000)
        undata = UsersCurrentAddress.objects.get(username = username)
        status = Booking_status.objects.get(cust_username= username)
        status.issue_resolved_status = '0'
        status.mech_assigned = '0'
        status.save()
        try :
            update = BookMechanic.objects.get(username = username)
            update.issueid = issueId
            update.Address = undata.address
            update.ZipCode = 560060
            update.vehicleNo = vehicleNumber
            update.phone = mobileNumber
            update.save()
        except:
            # udata = UsersCurrentAddress(issueid = '2',Address = undata.address,ZipCode = 560060 ,VehicleType = vehicleType,VehicleNo = vehicleNumber,Issuedesc = issueDescription,Phone = mobileNumber)
            undata.issueid = issueId
            undata.phone = mobileNumber
            undata.issuedesc = issueDescription
            undata.vehicleNo = vehicleNumber
            undata.vehicleType = vehicleType
            undata.issuetype = issuetype
            undata.issue_status_id = '0' # 0 for not booked 1 for booked 
            print("except called")
            undata.save()
        username = (request.session['cust_username'])
        print(username)
            # idata = UsersCurrentAddress(username=username,lat = latitude,lng = longitude)
            # idata.save()
        udata = UsersCurrentAddress.objects.get(username = username)
        latitude = udata.lat
        longitude = udata.lng
        udata.save()
            # if (UsersCustomer.objects.filter(username =username).exists() == True):
      
    
        key = settings.GOOGLE_API_KEY
            # eligable_locations = Locations.objects.filter(place_id__isnull=False)
        locations = []
        print("Called from login")
        for a in range(0,1): 
            data = {
                    "lat":float(latitude), 
                    "lng": float(longitude), 
                    "name":'',
                    }

            locations.append(data)

            print(locations)
        instance_ip_or_domain = '127.0.0.1'
        context = {
                "key": key, 
                "locations": locations,
                'instance_ip_or_domain': instance_ip_or_domain

        }
            
        return render(request, 'loading_bar.html', context)

        

    return render(request,"issue_detailpage.html") 
    
def accept_rules(request):
    return render(request,"accept_rules.html") 


def check_mechanic(request):
    cust_username = request.session['cust_username']
    status = Booking_status.objects.get(cust_username = cust_username )
    print(cust_username)
    booked = status.mech_assigned
    print(booked)
    
    if booked == '1':
        
        data = {'status': 'found'}
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 'not_found'})
    return JsonResponse(data)
    

def mech_booked(request):
    return render(request,"accept_rules.html") 

def profile(request):
    profile = Profile.objects.get(cust_username =request.session['cust_username'] )
    
    return render(request,"profile.html",{'phone' : profile.phone, 'rating' : profile.rating,'no_of_bookings':profile.no_of_bookings,'cust_name':profile.cust_name})


def check_booking_status(request):
    cust_username = request.session['cust_username']
    status = Booking_status.objects.get(cust_username = cust_username )
    issue_resolved = False  
    if(status.issue_resolved_status == '1'):
        issue_resolved = True  
        return JsonResponse({'issueResolved': issue_resolved})
    return JsonResponse({'issueResolved': issue_resolved})

def waiting_page(request):
    cust_username = request.session['cust_username']
    status = Booking_status.objects.get(cust_username = cust_username )
    if(status.issue_resolved_status == '0' and status.mech_assigned == '1'):
        mech_username = status.mech_username
        mech_name = status.mech_name
        cust_lat = status.cust_lat
        cust_lng = status.cust_lng
        mech_lat = status.mech_lat
        mech_lng = status.mech_lng
        duration_seconds = status.duration_seconds
        time_to_reach_minutes = (int(duration_seconds) // 60)
        booking_time = status.booking_time
        booking_time = datetime.strptime(booking_time, "%H:%M:%S")
        current_time = datetime.now() 
        customer_open_time = datetime.strptime(current_time.strftime('%H:%M:%S'), "%H:%M:%S")
        time_difference = customer_open_time - booking_time
        time_left_minutes = time_to_reach_minutes - time_difference.total_seconds() //60
        if(time_left_minutes < 0):
            time_left_minutes = 0
            
        key = settings.GOOGLE_API_KEY
        duration_kilometers = status.duration_kilometers
        mech = UsersMechanic.objects.get(username= mech_username)
        mech_add = MechanicDetails.objects.get(username = mech_username)
        locations = []
        data = {
            'cust_lat':float(cust_lat),
            'cust_lng':float(cust_lng),
            'mech_lat':float(mech_lat),
            'mech_lng':float(mech_lng)
        }
        print(cust_lat)
        locations.append(data)
        instance_ip_or_domain = '127.0.0.1'

        return render(request,'waiting_page.html',
                    {'card_data':mech_username,
                    'mech_name':mech_name,
                    'key':key,'duration_minutes':time_left_minutes * 60,
                    'distance_kilometers':duration_kilometers,
                    'locations' :locations,
                    'phone' : mech.mobile,
                    'address': mech_add.mech_Address,
                    'instance_ip_or_domain': instance_ip_or_domain
                    
                    })
    else:
        return render(request,"no_ongoing.html")

from .forms import FeedbackForm
def feedback(request):
    if request.method == 'POST':
        cust_username = request.session['cust_username']
        status = Booking_status.objects.get(cust_username = cust_username )
        # feedback_desc = request.POST.get('desc', '')
        
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            form.save()
        status.issue_resolved_status = 1
        status.mech_assigned = 0
        status.save()
        booking = Bookings(booking_time = status.booking_time,booking_date= status.booking_date,mech_name = status.mech_name ,cust_username =cust_username)
        mech_phone = UsersMechanic.objects.get(username = status.mech_username)
        booking.phone = mech_phone.mobile
        issue = UsersCurrentAddress.objects.get(username = cust_username)
        booking.issue_desc = issue.issuedesc
        booking.save()   
        no_of_bookings = Profile.objects.get(cust_username = cust_username)
        b = int(no_of_bookings.no_of_bookings)
        b += 1
        no_of_bookings.save()
        profile = Profile_mechanic.objects.get(mech_username = status.mech_username )
        profile.rating = 4

        profile.save()

        return redirect('home_page')
    else:
        form = FeedbackForm()
    return render(request,"feedback.html", {'form': form})

def home_page(request):
    return render(request,"landing_page.html") 

def Booking_histroy(request):
    cust_username = request.session['cust_username']
    bookings = []
    book_data = Bookings.objects.filter(cust_username = cust_username)
    for i in book_data:
        
        data = {
            "booking_time" : i.booking_time,
            "booking_date" : i.booking_date,
            "mech_name" : i.mech_name,
            
            "issue_desc" : i.issue_desc 
        }
        bookings.append(data)

    return render(request,"Bookings.html",{"bookings":bookings})

from django.contrib import messages
global no
no = 0
def otp(request):
    global no
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')

        entered_otp = f"{otp1}{otp2}{otp3}{otp4}"
        if (int(entered_otp) == int(no)):
            messages.success(request, 'OTP verified successfully!')
            email_status = UsersCustomer.objects.get(username = request.session['cust_username'])
            email_status.cust_email_verified = '1'
            email_status.save()
            return redirect('login')
        else:
            messages.success(request, 'OTP verified successfully!')
            return HttpResponse('invalid')
    else:
        mail = UsersCustomer.objects.get(username = request.session['cust_username'])
        no = random.randrange(1000,9999)
        subject = ''' Hello,
 
{} is your one-time passcode (OTP) for the ResQify app.
 
Uae the above OTP to register for ResQify App. 
 
The code was requested from the ResQify's App on google your device.It will be valid for 4 hours.
 
 
Enjoy the app!
 
ResQify's team'''
        send_mail('Your One Time Passcode for ResQify',subject.format(no),EMAIL_HOST_USER,[mail.email],fail_silently=True)
        return  render(request,"otp.html")