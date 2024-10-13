from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def news(request):
    return render(request, 'news.html')