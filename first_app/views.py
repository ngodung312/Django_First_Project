import imp
from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from first_app.models import Topic, Webpage, AccessRecord
from first_app import forms

# Create your views here.
def index(request):
    data = {'insert_text': 'List of pages:'}
    return render(request, 'first_app/index.html', data)


def main_page(request):
    data = {'insert_me': "From main page!"}
    return render(request, 'first_app/main_page.html', data)


def access_records(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_date = {'access_records': webpages_list}
    return render(request, 'first_app/access_records.html', date_date)


def user_form(request):
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print('NAME:', form.cleaned_data['name'])
            print('EMAIL:', form.cleaned_data['email'])
            print('TEXT:', form.cleaned_data['text'])

    return render(request, 'first_app/user_form.html', {'form': form})