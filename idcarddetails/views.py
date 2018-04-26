from django.http import HttpResponse
from django.template import loader

from allauth.account.views import LoginView
from allauth.account.forms import SignupForm, LoginForm
from .forms import IDCardNumbersForm
from .models import IDCardNumbers

class LoginAndSignUpView(LoginView):
	def get_context_data(self, **kwargs):
	    context = super(LoginAndSignUpView, self).get_context_data(**kwargs)
	    context.update({'signupform': SignupForm})
	    return context

def profile(request):
	template = loader.get_template('idcarddetails/profile.html')
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
	userCardDetails = IDCardNumbers.objects.filter(username=request.user.id)
	if userCardDetails.exists():
		return HttpResponse(template.render({'cardsDetails' : userCardDetails, 'detailsExist' : True}, request))
	else:
		context = {'idCardDetailsForm' : IDCardNumbersForm}
		return HttpResponse(template.render(context, request))
