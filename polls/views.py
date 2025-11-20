from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Hello, world. You're at the polls index.</h2>")

def about(request):
    return HttpResponse("<h2>About Us</h2>")

def contact(request):
    return HttpResponse("<h2>Contact Us</h2>")
