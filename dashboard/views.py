from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import item

@login_required
def index(request):
    items = item.objects.filter(create_bt=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })


