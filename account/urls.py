from django.urls import path, include
from account.views import UserRegistrationView, UserloginView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserloginView.as_view(), name='login'),
    path('forgotpassword/', ForgotPasswordView.as_view(), name = 'forgotpassword'),
]