from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('course/',views.course, name='course'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('course_code/',views.course_code, name='course_code'),
    path('logout/',views.logout, name='logout'),
    path('contactform/',views.contactform, name='contactform'),
]
