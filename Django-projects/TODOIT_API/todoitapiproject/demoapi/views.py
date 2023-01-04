from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def hello_world(request):
    return Response(
        {"message": "Hello, world :>"}, 
        status=status.HTTP_208_ALREADY_REPORTED
    )