from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

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