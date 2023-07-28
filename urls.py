
from django.urls import path
from . import views
urlpatterns = [
    
    path('stafflogin', views.stafflogin, name='stafflogin'),
    path('stafflogin/staffdashboard', views.staffdashboard, name='staffdashboard'),
    path('register',views.register, name ='register' ),
    
    
]


