from django.shortcuts import render

# Create your views here.
#settig front page
def index(request):
    return render(request , 'core/index.html')
def contact(request):
    return render(request , 'core/contact.html')
def term(request):
    return render(request , 'core/term.html')