from django.shortcuts import render, HttpResponse, redirect
from apps.login_app.models import User

def index(request):
    print('*'*50, 'showing the home page')
    if 'new_user_id' not in request.session:
        return render(request, "optima_app/index.html")
    else:
        user = User.objects.get(id=request.session['new_user_id'])
        context = {
            'user': user
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
