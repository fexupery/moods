from django.shortcuts import render
from .models import Mood

def all_moods(request):
    moods = Mood.objects.all()
    return render(request,'moods/all_moods.html',{'moods':moods})
