from django.htt import HttpResponse

def home(request):
    return HttpResponse("Homepage")