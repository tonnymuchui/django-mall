from django. import HttpResponse

def home(request):
    return HttpResponse("Homepage")