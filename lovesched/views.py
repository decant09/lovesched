from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def debug_static_url(request):
    return HttpResponse(f"STATIC_URL is set to: {settings.STATIC_URL}")

def debug_500(request):
    """ Temporary view to test 500.html rendering """
    return render(request, "errors/500.html", status=500)

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

def handler403(request, exception):
    """ Error Handler 403 - Forbidden """
    return render(request, "errors/403.html", status=403)

def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "errors/500.html", status=500)
