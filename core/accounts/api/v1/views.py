from rest_framework import generics
from .serializers import RegistrationsSerializer,CustomAuthTokenSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView



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