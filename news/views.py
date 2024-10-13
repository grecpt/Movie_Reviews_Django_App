from django.shortcuts import render

# Create your views here.
from .models import News

def news(request):
    newss = News.objects.all()
    return render(request, 'news.html',{'newss':newss})