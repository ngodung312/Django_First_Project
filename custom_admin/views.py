from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from custom_admin import forms, tasks


# Create your views here.
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
                return render(request, 'custom_admin/login.html', {'login_status': "Invalid username or password. Please try again!", 
                                                                'next': request.POST['next']})
            except:
                return render(request, 'custom_admin/login.html', {'login_status': "Invalid username or password. Please try again!"})

    else:
        try: 
            return render(request, 'custom_admin/login.html', {'next': request.GET['next']})
        except:
            return render(request, 'custom_admin/login.html')



@login_required
def user_logout(request):
    logout(request)
    return redirect('index')



def register(request):
    registered = False 

    if request.method == "POST":
        user_form = forms.LoginUserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']
            # tasks.modify_name(username=user.username)
            user.save()
            registered = True 
        else:
            print(user_form.errors, sep='\n')
    else:
        user_form = forms.LoginUserForm

    return render(request, 'custom_admin/registration.html', 
                        {   'user_form': user_form, 
                            'registered': registered    })
