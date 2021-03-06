from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,ListCreateAPIView
from KeepAccess.settings import SECRET_KEY
from Auth.models import *
from Auth.serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt , datetime


class UsersDefineAll(ListCreateAPIView):
        queryset =User.objects.all()
        serializer_class =UserSerializer
        pagination_class = None
        User.objects

class LoginView(APIView):
    def post(self, request):
        login= request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=login).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=240),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        response = Response()

        user = User.objects.get(username=login)        
        employes_serializer = UserSerializer(user) 

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token,
            'poste' : employes_serializer.data['poste']
        }

        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!!')

        user = User.objects.get(username=payload['id']) 
        employes_serializer = UserSerializer(user) 
        return Response(employes_serializer.data) 

class PropertiesUserUpdate(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=self.kwargs.get('pk', None))

