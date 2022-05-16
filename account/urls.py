from django.urls import path, include
from account.views import UserPasswordResetView, UserRegistrationView, UserloginView, SendPasswordResetEmailView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserloginView.as_view(), name='login'),
   path('reset/', SendPasswordResetEmailView.as_view(), name='reset'),
   path('userresetpassword/', UserPasswordResetView.as_view(), name = 'userresetpassword')
]