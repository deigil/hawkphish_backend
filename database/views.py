from django.shortcuts import render
from rest_framework import serializers


import json
from database.models import Links
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import LinkSerializer

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

    def post(self, request):
        # Parse the incoming JSON data
        try:
            data = json.loads(request.body)
            print(data)
            # parsed = json.loads(request)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON data"}, status=400)

        # Check if required fields are present
        # required_fields = ['domainURL', 'domainTitle', 'timeAccessed', 'domainRating']
        # for field in required_fields:
        #     if field not in data:
        #         return Response({"error": f"Missing required field: {field}"}, status=400)

        existing_link = Links.objects.filter(domainURL=data['domainURL']).first()

        if existing_link:
            # If an entry exists, increment clicked_count by 1
            existing_link.clicked_count += 1
            existing_link.save()
        else:
            # If no entry exists, create a new one
            link = Links(
                domainURL=data['domainURL'],
                domainTitle=data['domainTitle'],
                timeAccessed=data['timeAccessed'],
                domainRating=data['domainRating'],
                reasonNoHttps=data.get('reasonNoHttps'),
                reasonShortened=data.get('reasonShortened'),
                reasonAtSymbol=data.get('reasonAtSymbol'),
                reasonBadExtension=data.get('reasonBadExtension'),
                clicked_count=data.get('clicked_count', 1)  # Start clicked_count at 1 for new entries
            )
            link.save()

        # Return success response
        return Response({"message": "Link added successfully"}, status=201)
