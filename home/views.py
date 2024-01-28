from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# class called when signing up
class Signupview(CreateView):
    template_name = 'home/register.html'
    success_url = "fileman/dir/media"
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('directory_browse' 'media')
        return super().get(request, *args, **kwargs)

# class called when logging out
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

# class called when logging in
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

# the class view to the first page after signing in
class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {'today': datetime.today()}

# security class what deals with aurthorizations
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url='/admin'
