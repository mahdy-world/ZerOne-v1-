from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views import View
from django.views.generic import *
from django.urls import reverse_lazy

from Auth.forms import ChangePasswordForm


# Create your views here.
class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('Core:index')
            else:
                error = 'تم ايقاف الحساب الخاص بك '
                return render(request, 'login.html', context={'error': error})
        else:
                error = 'برجاء التأكد من اسم المستخدم وكلمة المرور'
                return render(request, 'login.html', context={'error': error})

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('Core:index')
        return render(request, 'login.html')


class Logout(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('Auth:login')


def ChangePassword(request):
    form = ChangePasswordForm(request.POST or None)
    action_url = reverse_lazy('Auth:ChangePassword')
    password = form["password"].value()
    title = "تغير كلمة المرور"
    
    context = {
        'title':title,
        'form': form,
        'action_url' : action_url
    }
    
    
    if form.is_valid():
        user = User.objects.get(username=request.user)
        user.set_password(password) 
        user.save()
        return redirect('Core:index')

    return render(request,'forms/form_template.html', context)        