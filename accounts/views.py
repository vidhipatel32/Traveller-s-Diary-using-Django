from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def signupacc(request):
    if request.method == "GET":
        return render(request,"signup.html",{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request,user)
                return redirect('home')
            except:
                return render(request,"signup.html",{'form':UserCreationForm, 'error':"Username is not Unique"})
        else:
            return render(request,"signup.html",{'form':UserCreationForm, 'error':"Password Do Not Match"})
     
def logoutacc(request):
    logout(request)
    return redirect('home')

def loginacc(request):
    if request.method=="GET":
        return render(request,"login.html",{'form':AuthenticationForm})
    else:
        user = authenticate(request,
                            username = request.POST['username'],
                            password = request.POST['password'])
        if user is None:
            return render(request,"login.html",{'form':AuthenticationForm,'error':"Username or Password Mismatch"})
        else:
            login(request,user)
            return redirect('home')