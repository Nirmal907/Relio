from django.shortcuts import render
from .models import *
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    # product=Product.objects.all()
    # n= len(product)
    # nSlides= n//4 + ceil((n//4)-n/4)
    # allProds=[[product, range(1,nSlides),nSlides],[product, range(1,nSlides),nSlides]]
    # params={'product':product, 'no_of_slides':nSlides, 'range':range(1,nSlides)}
    allProds=[]
    allcat= Product.objects.values('category','id')
    cats={item['category'] for item in allcat}
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
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def product(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")