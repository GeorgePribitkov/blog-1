from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .forms import RegisterUserForm

# Create your views here.
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    

    def get_success_url(self):
        return reverse_lazy('blog:post_list')

def login_user(request):
    return HttpResponse('logged in')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect (reverse('users:login'))

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect (reverse('users:login'))
    else:
        form = RegisterUserForm
    return render(request,'users/register.html', {'form': form})