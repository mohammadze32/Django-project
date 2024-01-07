from django.shortcuts import render , get_object_or_404
from .models import item
def detail(request , pk):
    items = get_object_or_404(item , pk=pk)
    print("HIHIHIHI")
    related_item = item.objects.filter(catagory=items.catagory , is_sold=False).exclude(pk=pk)
    print(related_item)
    return render(request , 'item/detail.html' , {
      'item' : items ,
      'related_item' : related_item
    })
