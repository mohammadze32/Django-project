from django.contrib import admin
from django.urls import path
from core.views import index
from core.views import contact , term
urlpatterns = [
    path('' , index , name = 'index ' ) ,
    path('admin/', admin.site.urls),
    path('contact/' , contact , name= 'contact'),
    path('term/' , term , name= 'term')
]
