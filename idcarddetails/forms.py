from django import forms

from .models import IDCardNumbers, AadharCardPhotos

class IDCardNumbersForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(IDCardNumbersForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
		    field = self.fields.get(field_name)  
		    if field:
		        if type(field.widget) in (forms.TextInput, forms.DateInput):
		            field.widget = forms.TextInput(attrs={'placeholder': field.label})

	class Meta:
		model = IDCardNumbers
		fields = ('aadharNumber', 'drivingLicenseNumber', 'voterCardNumber', 'rationCardNumber', 'passportNumber')

class AadharForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(AadharForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			field = self.fields.get(field_name)
			if field:
				if type(field.widget) in (forms.TextInput, forms.DateInput):
					field.widget = forms.TextInput(attrs={'placeholder' : field.label})

	class Meta:
		model = AadharCardPhotos
		fields = ('aadharPhoto',)

