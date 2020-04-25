from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'moods' #to reference all urls to moods and avoid mistakes with urls to others apps as portfolio

urlpatterns = [
    path('',views.all_moods,name='all_moods'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
