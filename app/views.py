from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    banners = Banner.objects.all()
    statistiks = Statistiks.objects.all()
    services = servise.objects.all()
    results = Result.objects.all()
    contacts = Contact.objects.all()
    revyu = Revyu.objects.all()
    social_accounts = Social_account.objects.all()
    context = {
        "banners": banners,
        "statistiks": statistiks,
        "services": services,
        "results": results,
        "contacts": contacts,
        "revyu": revyu,
        "social_accounts": social_accounts
    }
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        deegry = request.POST.get('deegry')
        contact_number = request.POST.get('contact_number')
        message = request.POST.get('message')
    
    # Contact.objects.create(
    #     first_name = first_name,
    #     last_name = last_name,
    #     contact_number = contact_number,
    #     deegry = deegry,
    #     message = message
    # )
    return render(request , 'index.html', context) 
def banner(request):
    banner = Banner.objects.all()
    context = {
        "banner": banner
    }
    return render(request, 'banner.html', context)  
def statistiks(request):
    statistiks = Statistiks.objects.all()
    context = {
        "statistiks": statistiks
    }
    return render(request,'statistiks.html', context)
def services(request):
    services = servise.objects.all()
    context = {
        "services": services
    }
    return render(request,'services.html', context)
def results(request):
    results = Result.objects.all()
    context = {
        "results": results
    }
    return render(request,'results.html', context)

def contact(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)
def revyu(request):
    revyu = Revyu.objects.all()
    context = {
        "revyu": revyu
    }
    return render(request,'revyu.html', context)
def social_accounts(request):
    social_accounts = Social_account.objects.all()
    context = {
        "social_accounts": social_accounts
    }
    return render(request,'social_accounts.html', context)

