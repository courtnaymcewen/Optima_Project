from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "optima_app/index.html")

def results (request):
    return render (request, "optima_app/results.html")
