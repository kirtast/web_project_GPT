from django.shortcuts import render
from django.http import HttpResponse

# View function for the home page
def home(request):
    # Return a simple HTTP response with the message 'Hello, world!'
    return HttpResponse('Hello, world!')

# View function for the about page
def about(request):
    # Render the 'about.html' template and return the resulting HTTP response
    return render(request, 'about.html')

# View function for the contact page
def contact(request):
    # Render the 'contact.html' template and return the resulting HTTP response
    return render(request, 'contact.html')
