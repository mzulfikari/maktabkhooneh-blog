from rest_framework import generics
from .serializers import RegistrationsSerializer,CustomAuthTokenSerializer,ChangePasswordSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
 
User = get_user_model() 

class RegistrationApiView(generics.GenericAPIView):
    """Implementation of email registration system and password check"""
    serializer_class = RegistrationsSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationsSerializer(data= request.data )
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer.validated_data['email']
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

class CustomAuthToken(ObtainAuthToken):
    """Personalization of the authentication system with the user's email and password"""
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
class CustomDiscaAuthToken(APIView):
    """Log out of the user and delete the generated token"""
    permission_classes = [IsAuthenticated]
    
    def post (self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
    
class ChangePasswordApiView(generics.GenericAPIView):
    """ To change user password by implementing advanced elements """
    model = User
    permission_classes =[IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    
    def get_object(self,queryset=None):
        obj = self.request.user
        return obj
    
    def put(self,request,*args,**kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password":["wrong password."]},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail':'password change successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)