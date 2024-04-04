from django.shortcuts import render
from database.models import *

def display_links(request):
    links = Links.objects.all()  # Retrieve all instances of the Links model
    return render(request, 'list_links.html', {'updatedLink': links})

def homepage(request):
    return render(request, 'homepage.html')

