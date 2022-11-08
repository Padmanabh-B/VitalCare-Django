from django.shortcuts import render,redirect
from .models import HeadCard,Card,Emergency,About,Services,Contact
# Create your views here.

def home(request):
    head = HeadCard.objects.all()
    card = Card.objects.all()
    emg = Emergency.objects.all()
    data = {
        'head':head,
        'card':card,
        'emg':emg,
    }
    return render (request, 'webpages/home.html',data)

def about(request):
    about = About.objects.all()
    data = {
        'about':about
    }
    return render (request, 'webpages/about.html',data)

def services(request):
    serv = Services.objects.all()
    data = {
        'serv' : serv,
    }
    return render (request, 'webpages/services.html',data)

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(fname=fname, address=address, email=email, phone=phone, message=message)
        contact.save()
        return redirect('home')
    return render (request, 'webpages/contact.html')