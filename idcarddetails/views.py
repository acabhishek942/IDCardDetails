from django.http import HttpResponse
from django.template import loader

from allauth.account.views import LoginView
from allauth.account.forms import SignupForm, LoginForm


def index(request):
    return HttpResponse("Hello, world. You're at the idcarddetails index.")

class LoginAndSignUpView(LoginView):
	def get_context_data(self, **kwargs):
	    context = super(LoginAndSignUpView, self).get_context_data(**kwargs)
	    context.update({'signupform': SignupForm})
	    return context

def profile(request):
	template = loader.get_template('idcarddetails/profile.html')
	return HttpResponse(template.render({}, request))
