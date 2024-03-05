from django.shortcuts import render
from rest_framework import serializers

from database.models import Links
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import LinkSerializer

@api_view(['GET'])
def getData(request):
    app = Links.objects.all()
    serializer = LinkSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = LinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @csrf_exempt  # For simplicity; use CSRF protection in production
# @require_POST
# def add_link(request):
#     try:
#         data = json.loads(request.body)
#         url = data.get('url')
#         # Additional parameters like shortened_url, suspicious_domain, no_https can be extracted similarly

#         # Check if the link already exists in the database
#         link, created = Links.objects.get_or_create(url = url)

#         if not created:
#             # If the link already exists, increment the clicked_count
#             link.clicked_count += 1
#             link.save()
#         return JsonResponse({'message': 'Link added successfully'})

#     except json.JSONDecodeError as e:
#         return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

class LinkCreateView(APIView):
    def get(self, request):
        network = Links.objects.all()
        serializer = Links(network, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            # Try to deserialize the incoming JSON data
            serializer = LinkSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)  # Raise an exception for invalid data

            # If valid, save the data
            serializer.save()

            # Print the received data
            print("Received data:", request.data)

            return Response(serializer.data, status=201)
        except serializers.ValidationError as e:
            # Handle validation errors
            print("Validation Error:", e)
            return Response({'error': 'Validation Error'}, status=400)
        except Exception as e:
            # Handle other exceptions
            print("Error:", e)
            return Response({'error': 'An error occurred'}, status=500)