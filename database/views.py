from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from database.models import Links

@csrf_exempt  # For simplicity; use CSRF protection in production
@require_POST
def add_link(request):
    try:
        data = json.loads(request.body)
        url = data.get('url')
        # Additional parameters like shortened_url, suspicious_domain, no_https can be extracted similarly

        # Check if the link already exists in the database
        link, created = Links.objects.get_or_create(url = url)

        if not created:
            # If the link already exists, increment the clicked_count
            link.clicked_count += 1
            link.save()
        return JsonResponse({'message': 'Link added successfully'})

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)