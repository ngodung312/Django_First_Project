from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from first_app.models import Topic, UserProfile, Webpage, AccessRecord
from first_app import forms


# Login 
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                try:
                    return redirect(request.POST['next'])
                except:
                    return redirect('index')
            else:
                try:
                    return render(request, 'first_app/login.html', {'login_status': "Account not active!", 
                                                                    'next': request.POST['next']})
                except:
                    return render(request, 'first_app/login.html', {'login_status': "Account not active!"})
        else:
            try:
                return render(request, 'first_app/login.html', {'login_status': "Invalid username or password. Please try again!", 
                                                                'next': request.POST['next']})
            except:
                return render(request, 'first_app/login.html', {'login_status': "Invalid username or password. Please try again!"})

    else:
        try: 
            return render(request, 'first_app/login.html', {'next': request.GET['next']})
        except:
            return render(request, 'first_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


# Create your views here.
def index(request):
    data = {'insert_text': 'List of pages:'}
    return render(request, 'first_app/index.html', data)


@login_required()
def main_page(request):
    data = {'insert_me': "From main page!"}
    return render(request, 'first_app/main_page.html', data)


@login_required
def access_records(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_date = {'access_records': webpages_list}
    return render(request, 'first_app/access_records.html', date_date)


@login_required
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


def register(request):
    registered = False 

    if request.method == "POST":
        user_form = forms.LoginUserForm(data=request.POST)
        profile_form = forms.UserProfileForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user 

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True 
        else:
            print(user_form.errors, profile_form.errors, sep='\n')
    else:
        user_form = forms.LoginUserForm
        profile_form = forms.UserProfileForm

    return render(request, 'first_app/registration.html', 
                        {   'user_form': user_form, 
                            'profile_form': profile_form,
                            'registered': registered    })
