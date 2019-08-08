from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from apps.login_app.models import User

def index(request):
    print('*'*50, 'showing the home page')
    print('index'*50, request.session['logged_in'])
    if 'new_user_id' not in request.session:
        return render(request, "optima_app/index.html")
    else:
        user = User.objects.get(id=request.session['new_user_id'])
        context = {
            'user': user,
            'logged_in': request.session['logged_in']
        }
        return render(request, "optima_app/index.html", context)

def results (request):
    print('*'*50, 'showing the results page')
    return render(request, "optima_app/results.html")

def show_account(request, user_id):
    print('*'*50, 'showing the update account page')
    if 'new_user_id' not in request.session:
        return redirect('/login')
    else:
        user = User.objects.get(id=user_id)
        context = {
            'user': user
        }
        return render(request, "optima_app/update_account.html", context)

def update_account(request, user_id):
    print('*'*50, 'the update account method is working')
    errors = User.objects.update_validator(request.POST)
    edit_this_user = User.objects.get(id=user_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/my_account/' + str(edit_this_user.id))
    else:
        edit_this_user.first_name = request.POST['first_name']
        edit_this_user.last_name = request.POST['last_name']
        edit_this_user.email_address = request.POST['email']
        hashed = bcrypt.hashpw(request.POST['password_reg'].encode(), bcrypt.gensalt())
        edit_this_user.password = hashed
        edit_this_user.save()
        return redirect('/my_account/' + str(edit_this_user.id))
    
