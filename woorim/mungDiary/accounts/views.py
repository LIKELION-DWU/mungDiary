from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def join(request):
    return render(request, 'join.html')