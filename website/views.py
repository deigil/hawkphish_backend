from django.shortcuts import render
from database.models import Links

def display_links(request):
    links = Links.objects.all()  # Retrieve all instances of the Links model
    return render(request, 'list_links.html', {'links': links})
