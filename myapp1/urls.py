from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='landing'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.homepage,name='home')

]