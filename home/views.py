from django.shortcuts import render

# Create your views here.

def index(request):
    """Index.html"""
    return render(request, 'home/index.html')
