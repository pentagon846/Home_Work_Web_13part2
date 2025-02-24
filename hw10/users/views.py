#all file new 4
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import RegisterForm


class RegisterViews(View):
    form_class = RegisterForm
    template_name = "users/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:root")
        return super(RegisterViews, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form":self.form_class})
    
    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Вітаю {username}! Ваш акаунт успішно створений ")
            return redirect(to="users:login")
        return render(request, self.template_name, {"form": form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'

        
