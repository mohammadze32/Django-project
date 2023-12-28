from django.contrib import admin
from django.urls import path
from core.views import index
from core.views import contact
urlpatterns = [
    path('' , index , name = 'index ' ) ,
    path('admin/', admin.site.urls),
    path('contact/' , contact)
]
