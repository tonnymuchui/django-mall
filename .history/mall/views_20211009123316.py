from django.h import HttpResponse

def home(request):
    return HttpResponse("Homepage")