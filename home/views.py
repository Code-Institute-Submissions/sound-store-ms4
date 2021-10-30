from django.shortcuts import render

# Create your views here.

def index(request):
    """Index.html"""
    return render(request, 'home/index.html')


# Error Handling
def error_404(request, exception):
    return render(request, '404.html')

def error_500(request, exception):
    return render(request, '500.html')

def error_403(request, exception):
    return render(request, '403.html')

def error_400(request, exception):
    return render(request, '400.html')
