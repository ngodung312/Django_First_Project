from django.urls import path
from first_app import views 

app_name = 'first_app'

urlpatterns = [
    path(r'', views.main_page, name='main_page'),
    path(r'access-records/', views.access_records, name='access_records'),
    path(r'user-form/', views.user_form, name='user_form'),
    path(r'registration/', views.register, name='registration'),
]