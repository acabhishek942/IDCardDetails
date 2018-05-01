from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^login/', views.LoginAndSignUpView.as_view(), name='loginandsignup'),
    url(r'^profile/', views.profile, name='idcarddetailsProfile'),
    url(r'^aadhar/', views.aadhar, name='aadharDetails'),
    url(r'^dl/', views.drivingLicense, name='drivingLicenseDetails'),
    url(r'^voter/', views.voter, name='voterDetails'),
    url(r'^ration/', views.ration, name='rationCardDetails'),
    url(r'^passport/', views.passport, name='passportDetails'),
]