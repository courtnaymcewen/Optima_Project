from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User
# Create your views here.
def show_login(request):
    print('the login and registration page is being displayed')
    return render(request, 'login_app/index.html')

def success(request):
    print('currently displaying the success page!')
    if 'new_user_id' not in request.session:
        return redirect('/login')
    else:
        return render(request, 'login_app/success.html')

def add_user(request):
    print('*'*50)
    print('the add user method is running!')
    print('password: ', request.POST["password_reg"])
    print('password conf: ', request.POST["confirm_password_reg"])
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="register")
        return redirect('/login')
    else:
        print('*'*50, 'creating user')
        hashed = bcrypt.hashpw(request.POST['password_reg'].encode(), bcrypt.gensalt())
        #decoded_hash = hashed.decode()
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email_address=request.POST["email"], password=hashed)
        new_user = User.objects.last()
        request.session['new_user_id'] = new_user.id
        request.session['name'] = new_user.first_name
        request.session['logged_in'] = 1
        return redirect('/')

def process_login(request):
    print('the login method is running')
    print('*'*50, request.POST)
    errors = User.objects.login_validator(request.POST)
    print('*'*50, errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login")
        return redirect('/login')
    else:
        print('*'*50, 'log in successful')
        user_matches = User.objects.filter(email_address=request.POST['email_log'])
        if len(user_matches) == 0:
            messages.error(request, 'Email not found, please register', extra_tags="login")
            return redirect('/login')
        else:
            if bcrypt.checkpw(request.POST['password_log'].encode(), user_matches[0].password.encode()):
                request.session['new_user_id'] = user_matches[0].id
                request.session['name'] = user_matches[0].first_name
                request.session['logged_in'] = 1
                return redirect('/')
            else:
                print('!'*50)
                messages.error(request, 'Incorrect login credentials', extra_tags="login")
                print('incorrect password has been entered')
                return redirect('/login')

def logout(request):
    print('before'*50, request.session['logged_in'])
    print('the logout method is running')
    request.session.clear()
    request.session['logged_in'] = 0
    print('after'*50, request.session['logged_in'])
    return redirect('/')