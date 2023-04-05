from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm

def index(request):
  '''
  비로그인 상태
  AnonymousUser 출력
  로그인 페이지 이동 버튼
  로그인 상태
  로그인 사용자의 username 출력
  로그아웃 버튼'''
  return render(request,'accounts/index.html')

'''
로그인 페이지 GET
로그인 실행 POST'''
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        #AuthenticationForm 유효성 검사 통과 시 로그인
        if form.is_valid():
            auth_login(request,form.get_user())
            #redirect GET accounts/
            return redirect('accounts:index')

    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
        
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html',context)

def delete(request):
    request.user.delete()
    return redirect('accounts:index')


def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            return redirect('accounts:index')
    else:
        #userchageform으로 인스턴스 만들고, context로 넘겨서 출력
        form = CustomUserChangeForm()
        context = {
            'form':form,
        }
        return render(request,'accounts/update.html',context)

def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/change_password.html',context)