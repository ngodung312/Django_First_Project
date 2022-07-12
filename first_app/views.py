from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid:        
            try:
                form.save()
                print("VALIDATION SUCCESS!")
                print('NAME:', form.cleaned_data['name'])
                print('EMAIL:', form.cleaned_data['email'])
                print('VERIFY EMAIL:', form.cleaned_data['verify_email'])  
                return redirect("user_form")
            except:
                return render(request, 'first_app/user_form.html', {'form': form})
    else:
        form = forms.UserForm()
        return render(request, 'first_app/user_form.html', {'form': form})