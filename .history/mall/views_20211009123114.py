from django import request

def home(request):
    return HttpResponse("Homepage")