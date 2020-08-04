from django.shortcuts import render
from .models import *
from math import ceil
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse

def index(request):
    # product=Product.objects.all()
    # n= len(product)
    # nSlides= n//4 + ceil((n//4)-n/4)
    # allProds=[[product, range(1,nSlides),nSlides],[product, range(1,nSlides),nSlides]]
    # params={'product':product, 'no_of_slides':nSlides, 'range':range(1,nSlides)}
    # user = User.objects.values('username')
    # print(user)
    allProds=[]
    allcat= Product.objects.values('category','id')
    cats={item['category'] for item in allcat}
    # print(cats)
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    # print(type(cats))
    # for cat in allcat:
    print(allProds)
    params={'allProds':allProds}
    return render(request, 'index.html',params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', 'df')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')

def tracker(request):
    return render(request, 'tracker.html')

def search(request):
    return render(request, 'search.html')

def products(request,myid):
    # Fetching the product using the id
    product = Product.objects.get(id=myid)
    print(myid)
    print(product.product_id)
    return render(request, 'product.html',{'product':product})

def checkout(request):
    return render(request, 'checkout.html')