from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {'insert_me': "From views.py!"}
    return render(request, 'first_app/first_app.html', data)
