from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.http import JsonResponse

from .forms import SignUpForm

class FrontPageView(View):
    view_name = "frontpage"
    def get(self, request):
        return render(request, 'registerApp/frontpage.html', {'context':''})

class SignUpView(View):
    view_name = "signup"
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registerApp/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
        else:
            return render(request, 'registerApp/signup.html', {'form': form})

class CustomLoginView(LoginView):
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse({'success': False, 'errors': form.errors})
        return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'success': True})
        return response
