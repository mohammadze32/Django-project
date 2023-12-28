from django.shortcuts import render
from item.models import Catagory , item

# Create your views here.
#settig front page
def index(request):
    items = item.objects.filter(is_sold=False)[0:2]
    catagories = Catagory.objects.all()

    return render(request , 'core/index.html' , {
        'catagories' : catagories  ,
        'itema' : items ,
    })
def contact(request):
    return render(request , 'core/contact.html')
def term(request):
    return render(request , 'core/term.html')