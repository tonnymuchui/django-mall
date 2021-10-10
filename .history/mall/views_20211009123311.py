from dj import HttpResponse

def home(request):
    return HttpResponse("Homepage")