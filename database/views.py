from django.shortcuts import render
from rest_framework import serializers


import json
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

class LinksAPI(APIView):
    def get(self, request):
        link_url = request.GET.get('domainURL', None)
        if not link_url:
            return Response({"error": "Please provide a domainURL in the query parameters"}, status=400)
        try:
            # Try to retrieve the link from the database
            link = Links.objects.get(domainURL = link_url)
            serializer = LinkSerializer(link)
            return Response(serializer.data, status=200)
        except Links.DoesNotExist:
            return Response({"message": "Link not found"}, status=400)

        # network = Links.objects.all()
        # serializer = Links(network, many=True)
        # return Response(serializer.data)

    def post(self, request):
        # Parse the incoming JSON data
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON data"}, status=400)

        # Check if required fields are present
        required_fields = ['domainURL', 'domainTitle', 'timeAccessed', 'domainRating']
        for field in required_fields:
            if field not in data:
                return Response({"error": f"Missing required field: {field}"}, status=400)

        # Add the link to the database
        link = Links(
            domainURL = data['domainURL'],
            domainTitle = data['domainTitle'],
            timeAccessed = data['timeAccessed'],
            domainRating = data['domainRating'],
            reasonNoHttps = data.get('reasonNoHttps'),
            reasonShortened = data.get('reasonShortened'),
            reasonAtSymbol = data.get('reasonAtSymbol'),
            reasonBadExtension = data.get('reasonBadExtension'),
            clicked_count=data.get('clicked_count')
        )
        link.save()

        # Return success response
        return Response({"message": "Link added successfully"}, status=201)

    # def post(self, request):
    #     # Deserialize the incoming JSON data using the serializer
    #     serializer = LinkSerializer(data=request.data)
        
    #     # Check if the data is valid
    #     if serializer.is_valid():
    #         # If valid, save the data to the database
    #         serializer.save()
    #         # Return a success response with the serialized data
    #         return Response(serializer.data, status=201)
    #     else:
    #         # If data is invalid, return error response with serializer errors
    #         return Response(serializer.errors, status=400)

    # def post(self, request):
    #     # try:
    #         # Try to deserialize the incoming JSON data

    #         # parsed = json.loads(request)

    #         # print(parsed)

    #         serializer = LinkSerializer(data=request.data)
    #         if serializer.is_valid(raise_exception=True):  # Raise an exception for invalid data

    #             # If valid, save the data
    #             serializer.save()

    #             # Print the received data
    #             print("Received data:", request.data)
    #             return Response(serializer.data, status=201)
            
    #         print("Received data:", request.data)
    #         return Response(serializer.errors, status=400)
        # except serializers.ValidationError as e:
        #     # Handle validation errors
        #     print("Validation Error:", e)
        #     return Response({'error': 'Validation Error'}, status=400)
        # except Exception as e:
        #     # Handle other exceptions
        #     print("Error:", e)
        #     return Response({'error': 'An error occurred'}, status=500)