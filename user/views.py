from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import EndUser



@api_view(['POST'])
@csrf_exempt
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        user = EndUser.objects.create_user(username=username, password=password)
        if user:
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@csrf_exempt
def logout_view(request):
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)
