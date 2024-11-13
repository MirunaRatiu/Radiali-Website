from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here= fct(request)->response
# we can pull data from db/transform/send email
def index(request):
    products =  Product.objects.all()
    #return HttpResponse('Hello world new product');
    #map this view to an URL
    #when we get a request to that URL, this function will be called

    return render(request,'index.html',{'products' : products})
#template to return HTML to a client
#instead of returning an HttpResponse, we use render to render a template and 
#and return HTML markup tu a client