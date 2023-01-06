from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from todoitapiproject.logger import logging

logger = logging.getLogger('demoapi')

DEMO_PARAM = openapi.Parameter('demo_text', openapi.IN_QUERY, description='Usage example', required=True, type=openapi.TYPE_STRING)
DEMO_POST_PARAM = openapi.Schema(type='object')
DEMO_POST_RESPONSE = openapi.Schema(type='object')

# Create your views here.
@swagger_auto_schema(method='get', tags=['demo'], manual_parameters=[DEMO_PARAM])
@swagger_auto_schema(method='post', tags=['demo'], request_body=DEMO_POST_PARAM, responses={201: DEMO_POST_RESPONSE})
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        demo_text = request.GET.get('demo_text')
        logger.debug('GET test is good :>')
        return Response(
            {"message": f"Hello, world :> your text is '{demo_text}'!"}, 
            status=status.HTTP_208_ALREADY_REPORTED
        )
    if request.method == 'POST':
        demo_text = request.data.get('demo_text')
        logger.debug('POST test is good :>')
        return Response(
            {"message": f"Hello, world :> api works correctly with POST! your text is '{demo_text}'!"}, 
            status=status.HTTP_201_CREATED
        )