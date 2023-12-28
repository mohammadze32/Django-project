from django.shortcuts import render
from item.models import Catagory , item

def index(request):
    items = item.objects.filter(is_sold=False)[0:2]
    print(items)
    catagories = Catagory.objects.all()

    return render(request , 'core/index.html' , {
        'catagories' : catagories  ,
        'items' : items ,
    })
def contact(request):
    return render(request , 'core/contact.html')
def term(request):
    return render(request , 'core/term.html')