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
            return redirect('login') # 회원가입하면 로그인페이지로 이동
    return render(request, 'join.html')

# 로그인
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('로그인 성공')
            return redirect('home') ## 경로는 메인페이지로(세연이가 만든 메인페이지로 넘어가야됨)
        #else: 
            #return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html') 
    
# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')
    

