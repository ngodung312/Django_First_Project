from django.urls import path
from first_app import views 

app_name = 'first_app'

urlpatterns = [
    path(r'', views.main_page, name='main_page'),
    path(r'access_records/', views.access_records, name='access_records'),
    path(r'user_form/', views.user_form, name='user_form'),
]