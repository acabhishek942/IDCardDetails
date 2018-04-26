from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^login/', views.LoginAndSignUpView.as_view(), name='loginandsignup'),
    url(r'^profile/', views.profile, name='idcarddetailsProfile'),
]