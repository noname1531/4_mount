from django.shortcuts import render

from apps.about.models import Settings
# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    return render(request, 'index2.html', locals())