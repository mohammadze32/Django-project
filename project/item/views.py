from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm , OrderForm
from .models import Catagory, item as Item

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Catagory.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(catagory=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        print(item.catagory)
        form = OrderForm(request.POST)
        item1 = form.save()
        return redirect('/')
    print(item.catagory)

    #related_items = Item.objects.filter(catagory = item.catagory).exclude(pk=pk)[0:3]
    form = OrderForm()
    return render(request, 'item/detail.html', {
        'form' : form ,
        'item': item,
        'related_items': None
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.create_bt = request.user
            item.save()
            form.save_m2m()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, create_bt=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)#instance bekhatere error redierct

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, create_bt=request.user)
    item.delete()

    return redirect('dashboard:index')