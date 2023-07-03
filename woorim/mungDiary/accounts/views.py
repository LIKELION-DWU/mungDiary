from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# 회원가입
def signup(request):
    if request.method == "POST":
        if request.POST['password']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # login에 request와 새로 생성한 new_user 객체 넣어서 로그인 실행
            auth.login(request, new_user)
            print('회원가입 성공')
            return redirect('signup') # 경로는 메인페이지로(세연부분)
    return render(request, 'join.html')

# 로그인
def login(request):
    return render(request, 'login.html')
