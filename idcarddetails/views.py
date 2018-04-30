from django.http import HttpResponse
from django.template import loader

from allauth.account.views import LoginView
from allauth.account.forms import SignupForm, LoginForm
from .forms import IDCardNumbersForm, AadharForm, DrivingLicenseForm, VoterCardForm, RartionCardForm, PassPortForm
from .models import IDCardNumbers, AadharCardPhotos, DrivingLicensePhotos, VoterCardPhotos, RationCardPhotos, PassportPhotos

class LoginAndSignUpView(LoginView):
	def get_context_data(self, **kwargs):
	    context = super(LoginAndSignUpView, self).get_context_data(**kwargs)
	    context.update({'signupform': SignupForm})
	    return context

def profile(request):
	template = loader.get_template('idcarddetails/profile.html')

	# when request.method is 'POST' we need to perform validations
	# and save the data in DB.
	if request.method == 'POST':
		idcardForm = IDCardNumbersForm(request.POST)
		if idcardForm.is_valid():
			aadharNumber = idcardForm.cleaned_data['aadharNumber']
			drivingLicenseNumber = idcardForm.cleaned_data['drivingLicenseNumber']
			voterCardNumber = idcardForm.cleaned_data['voterCardNumber']
			rationCardNumber = idcardForm.cleaned_data['rationCardNumber']
			passportNumber = idcardForm.cleaned_data['passportNumber']
			userCardsDetails = IDCardNumbers(request.user.id, aadharNumber, drivingLicenseNumber, 
				voterCardNumber, rationCardNumber, passportNumber)
			userCardsDetails.save()
			return HttpResponse(template.render({'cardsDetails' : [userCardsDetails], 'detailsExist' : True}, request))

	# Search for the details in DB if already existing we pass the
	# 'detilsExist' flat to not render the form part of the template
	userCardDetails = IDCardNumbers.objects.filter(username=request.user.id)
	if userCardDetails.exists():
		return HttpResponse(template.render({'cardsDetails' : userCardDetails, 'detailsExist' : True}, request))
	else:
		context = {'idCardDetailsForm' : IDCardNumbersForm}
		return HttpResponse(template.render(context, request))

def aadhar(request):
	template = loader.get_template('idcarddetails/aadhar.html')

	if (request.method == 'POST' and request.FILES.get('aadharPhoto', False)):
		aadharForm = AadharForm(request.POST, request.FILES)
		if aadharForm.is_valid():
			aadharPhoto = AadharCardPhotos(username=request.user, aadharPhoto=request.FILES.get('aadharPhoto', False))
			aadharPhoto.save()
			return HttpResponse(template.render({'detailsExist' : True}, request))
	aadharPhotos = AadharCardPhotos.objects.filter(username=request.user.id)
	if aadharPhotos.exists():
		return HttpResponse(template.render({'aadharPhotos' : aadharPhotos, 'detailsExist' : True}, request))
	context = {'aadharForm' : AadharForm}
	return HttpResponse(template.render(context, request))

def drivingLicense(requets):
	template = loader.get_template('idcarddetails/drivingLicense.html')

	if (request.method == 'POST' and request.FILES.get('drivingLicensePhoto', False)):
		drivingLicenseForm  = DrivingLicenseForm(request.POST, request.FILES)
		if drivingLicenseForm.is_valid():
			drivingLicensePhoto = DrivingLicensePhotos(username=request.user, drivingLicensePhoto=request.FILES.get('drivingLicensePhoto', False))
			drivingLicensePhoto.save()
			return HttpResponse(template.render({'detailsExist' : True}, request))
	drivingLicensePhotos = DrivingLicensePhotos.objects.filter(username=request.user.id)
	if drivingLicensePhotos.exists():
		return HttpResponse(template.render({'drivingLicensePhotos' : drivingLicensePhotos, 'detailsExist' : True}, request))
	context = {'drivingLicenseForm'  : DrivingLicenseForm}
	return HttpResponse(template.render(context, request))

def voter(request):
	template = loader.get_template('idcarddetails/voterCard.html')

	if (request.method == 'POST' and request.FILES.get('voterCardPhoto', False)):
		voterCardForm = VoterCardForm(request.POST, request.FILES)

		if voterCardForm.is_valid():
			voterCardPhoto = VoterCardPhotos(username=request.user, voterCardPhoto=request.FILES.get('voterCardPhoto', False))
			voterCardPhoto.save()
			return HttpResponse(template.render({'detailsExist' : True}, request))
	voterCardPhotos = VoterCardPhotos.objects.filter(username=request.user.id)
	if voterCardPhotos.exists():
		return HttpResponse(template.render({'voterCardPhotos' : voterCardPhotos, 'detailsExist' : True}, request))
	context = {'voterCardForm' : VoterCardForm}
	return HttpResponse(template.render(context, request))

def ration(request):
	template = loader.get_template('idcarddetails/rationCard.html')

	if (request.method == 'POST' and request.FILES.get('rationCardPhoto', False)):
		rationCardForm = RartionCardForm(request.POST, request.FILES)

		if rationCardForm.is_valid():
			rationCardPhoto = RationCardPhotos(username=request.user, voterCardPhoto=request.FILES.get('rationCardPhoto', False))
			rationCardPhoto.save()
			return HttpResponse(template.render({'detailsExist' : True}, request))
	rationCardPhotos = RationCardPhotos.objects.filter(username=request.user.id)
	if rationCardPhotos.exists():
		return HttpResponse(template.render({'rationCardPhotos' : rationCardPhotos, 'detailsExist' : True}, request))
	context = {'rationCardForm' : RartionCardForm}
	return HttpResponse(template.render(context, request))

def passport(request):
	template = loader.get_template('idcarddetails/passPort.html')

	if (request.method == 'POST' and request.FILES.get('passportPhoto', False)):
		passportForm = PassPortForm(request.POST, request.FILES)

		if passportForm.is_valid():
			passportPhoto = PassportPhotos(username=request.user, voterCardPhoto=request.FILES.get('rationCardPhoto', False))
			passportPhoto.save()
			return HttpResponse(template.render({'detailsExist' : True}, request))
	passportPhotos = PassportPhotos.objects.filter(username=request.user.id)
	if passportPhotos.exists():
		return HttpResponse(template.render({'passportPhotos' : passportPhotos, 'detailsExist' : True}, request))
	context = {'passportForm' : PassPortForm}
	return HttpResponse(template.render(context, request))
