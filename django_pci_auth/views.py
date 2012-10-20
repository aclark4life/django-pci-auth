from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>django-pci-auth</h1><a href='/admin'>Admin</a>")
