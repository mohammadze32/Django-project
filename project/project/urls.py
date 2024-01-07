from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from core.views import index
from core.views import contact , term
urlpatterns = [
    path('' , index , name = 'index ' ) ,
    path('item/' , include('item.urls')),
    path('admin/', admin.site.urls),
    #path('contact/' , contact , name= 'contact'),
    #path('term/', term , name= 'term')
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
