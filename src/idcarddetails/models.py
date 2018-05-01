from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def user_aadhar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/aadhar/<filename>
    return 'user_{0}/aadhar/{1}'.format(instance.username.id, filename)

def user_drivingLicense_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/license/<filename>
    return 'user_{0}/license/{1}'.format(instance.username.id, filename)

def user_voterCard_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/voter/<filename>
    return 'user_{0}/voter/{1}'.format(instance.username.id, filename)

def user_rationCard_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/ration/<filename>
    return 'user_{0}/ration/{1}'.format(instance.username.id, filename)

def user_passport_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/passport/<filename>
    return 'user_{0}/passport/{1}'.format(instance.username.id, filename)

class IDCardNumbers(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	aadharNumber = models.CharField(max_length=20, unique=True)
	drivingLicenseNumber = models.CharField(max_length=20, unique=True)
	voterCardNumber = models.CharField(max_length=20, unique=True)
	rationCardNumber = models.CharField(max_length=20, unique=True)
	passportNumber = models.CharField(max_length=20, unique=True)

class AadharCardPhotos(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	aadharPhoto = models.ImageField(upload_to=user_aadhar_path)

class DrivingLicensePhotos(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	drivingLicensePhoto = models.ImageField(upload_to=user_drivingLicense_path)

class VoterCardPhotos(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	voterCardPhoto = models.ImageField(upload_to=user_voterCard_path)

class RationCardPhotos(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	rationCardPhoto = models.ImageField(upload_to=user_rationCard_path)

class PassportPhotos(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	passportPhoto = models.ImageField(upload_to=user_passport_path)

