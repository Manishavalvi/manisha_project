from time import time
from django.conf import settings
import random
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *
from django.core.mail import send_mail
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# Create your views here.

def index(request):
    doctorlist=Doctor.objects.all()
               
    return render(request,'index.html',{"doctorlist":doctorlist})
    
def header(request):
    return render(request,'header.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    if request.method =='GET':
        return render(request,'contact.html') 

    else:
        
        contact_data =  {
            'f_name' : request.POST['fname'],
            'c_email' : request.POST['email'],
            'c_subject' : request.POST['sub'],
            'c_message' : request.POST['msg'],
            
        }
        Contact.objects.create(
            full_name = contact_data['f_name'],
            email = contact_data['c_email'],
            subject = contact_data['c_subject'],
            message = contact_data['c_message'],

        )
        return render(request,'index.html',{'msg':'contact you soon'})
        


def paymentfail(request):
    return render(request,'paymentfail.html')


def payment(request):
    return render(request,'payment.html')


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
    
def appointment(request):
    if request.method =='GET':
        return render(request,'appointment.html')   
    else:
        global user_data
        user_data =  {
                        
                        
                        'fname' : request.POST['fname'],
                        'lname' : request.POST['lname'],
                        'email' : request.POST['email'],
                        'mobile' : request.POST['mobile'],
                        'date' : request.POST['date'],
                        'time' : request.POST['time'],
                    }

                    
        global c_otp
        c_otp = random.randint(100_000,999_999)
        subject = 'Book Appointment'
        message = f'hello {user_data["fname"]}  \n Your OTP is {c_otp}.'
        send_mail(subject, message, settings.EMAIL_HOST_USER,[user_data['email']])
                    
        currency = 'INR'
        amount = 50000  # Rs. 500
    
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler/'
    
        # we need to pass these details to frontend.
        global context
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        
        
        return render(request, 'otp.html', {'msg': 'check your mailbox!!'})
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            # result = razorpay_client.utility.verify_payment_signature(
            #     params_dict)
            # if result is not None:
            amount = 50000  # Rs. 500
            try:

                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)
                

                            # render success page on successful caputre of payment

                return render(request,'appointment.html',{'msg':'Appointment Successfully Booked'})


            except:

                # if there is an error while capturing payment.
                return render(request, 'paymentfail.html')
            # else:
 
            #     # if signature verification fails.
            #     return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
           # if other than POST request is made.
        return HttpResponseBadRequest()
        


def otp(request):
    if c_otp == int(request.POST['uotp']):
        AppoUser.objects.create (
        
                        
            f_name = user_data['fname'],
            l_name = user_data['lname'],
            email = user_data['email'],
            mobile = user_data['mobile'],
            date = user_data['date'],
            time = user_data['time'],
        )

        return render(request, 'payment.html', context = context)
    else:
        return render(request,'otp.html',{'msg':'Invalid OTP'})

 
def doctor(request):
    doctorlist=Doctor.objects.all()
               
    return render(request,'doctor.html',{"doctorlist":doctorlist})

