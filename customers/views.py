from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = forms.SignUpForm()
    return render(request, 'sign_up.html', {'form': form, 'type': 'Sign Up'})

class UserLoginView(LoginView):
    template_name = 'sign_up.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password!')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserDataForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Invalid data!')
    else:
        profile_form = forms.ChangeUserDataForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': profile_form})

@method_decorator(login_required, name='dispatch')
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    form_class = PasswordChangeForm

    def get_success_url(self):
        return reverse_lazy('change_password')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid data!')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
