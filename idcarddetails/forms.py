from django import forms

from .models import IDCardNumbers

class IDCardNumbersForm(forms.ModelForm):

	class Meta:
		model = IDCardNumbers
		fields = ('aadharNumber', 'drivingLicenseNumber', 'voterCardNumber', 'rationCardNumber', 'passportNumber')