from email import message
from urllib import response
from account.serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  access_token = AccessToken()
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Successful'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserloginView(APIView):
    def post(self, request):
        
        email = request.data['email']
        print(email)
        password = request.data['password']
        print(password)
        
        if not User.objects.filter(email=email).exists():
            return Response({"data": "No user exists for this creds"})

        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class ForgotPasswordView(APIView):
    def post(self, request):
        pass