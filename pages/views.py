from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")


def about(request):
    return HttpResponse("<h1>About Us</h1><p>This is the About page.</p>")


def contact(request):
    return HttpResponse("<h1>Contact Us</h1><p>Contact page content here.</p>")
