from django.urls import path
from accounts.views import UserRegisterView, UserSignInView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('login/', UserSignInView.as_view(), name='login user')
)
