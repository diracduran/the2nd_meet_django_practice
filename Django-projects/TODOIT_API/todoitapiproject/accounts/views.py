from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, parser_classes, renderer_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import status
from accounts.serializers import MyTokenObtainPairSerializer
from accounts.serializers import UserSerializer

# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def signin(request):
    if not all([request.data.get('first_name'), request.data.get('last_name'), request.data.get('email')]):
        return Response({'message': 'data is wrong :<'}, status=status.HTTP_400_BAD_REQUEST)
    if request.data.get('password') == request.data.get('password1'):
        task_serializer = UserSerializer(data=request.data)
        if task_serializer.is_valid():
            user = task_serializer.save()
            token = Token.objects.get(user=user)
            user_details = {}
            user_details.update({
                'token': token.key,
                'username': user.username
            })
            login(request=request, user=user)
            return Response(user_details, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'data is wrong :<'}, status=status.HTTP_400_BAD_REQUEST)