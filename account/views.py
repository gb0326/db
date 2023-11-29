from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.views import View

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('/')  # 로그인 성공 후 이동할 URL

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if form.errors:
            messages.error(self.request, "아이디 또는 비밀번호가 잘못되었습니다. 다시 시도해주세요.")
        return response
    
class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입이 완료되었습니다. 로그인해주세요!')
            return redirect('account:login')  # 회원가입 후 로그인 페이지로 이동
        else:
            messages.error(request, '입력한 정보가 올바르지 않습니다. 다시 시도해주세요.')
        return render(request, 'account/register.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # 회원가입 후 홈페이지로 이동
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

class RestrictedLoginView(CustomLoginView):
    pass