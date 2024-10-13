from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def news(request):
    newss = News.objects.all()
    return render(request, 'news.html',{'newss':newss})