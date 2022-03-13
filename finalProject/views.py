from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def homepage(request):
    return render(request, 'homepage.html')

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in
            user = form.get_user()
            login(request, user)
            return render(request,'homepage.html')
    else:
        form= AuthenticationForm()    
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')