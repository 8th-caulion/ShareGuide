from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def main(request):
    return render(request, 'main.html')

def signup(request):
    # 회원가입 기능
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password2"]
            )
            auth.login(request,user)
            return redirect('main')
    # request를 받은 곳에 signup.html을 보여줘!
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password =  password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render (request, 'signin.html', {'error': 'username or password is incorrect'})
    return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('main')