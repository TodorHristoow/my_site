from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model

from accounts.forms import UserCreateForm

UserModel = get_user_model()


class UserSignInView(auth_views.LoginView):
    template_name = 'accounts/sign-in.html'


class UserRegisterView(views.CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')
