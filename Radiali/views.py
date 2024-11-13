#request handler/action
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here= fct(request)->response
# we can pull data from db/transform/send email
def say_hello(request):
    #return HttpResponse('Hello world');
    #map this view to an URL
    #when we get a request to that URL, this function will be called

    return render(request,'hello.html',{'name':'Miruna'})
#template to return HTML to a client
#instead of returning an HttpResponse, we use render to render a template and 
#and return HTML markup tu a client