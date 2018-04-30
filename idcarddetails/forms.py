from django import forms

from .models import IDCardNumbers, AadharCardPhotos, DrivingLicensePhotos, VoterCardPhotos, RationCardPhotos, PassportPhotos

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

class DrivingLicenseForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(DrivingLicenseForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			if field:
				if type(field.widget) in (forms.TextInput, forms.DateInput):
					filed.widget = form.TextInput(attrs={'placeholder' : field.label})

	class Meta:
		model = DrivingLicensePhotos
		fields = ('drivingLicensePhoto',)


class VoterCardForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(VoterCardForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			if field:
				if type(field.widget) in (forms.TextInput, forms.DateInput):
					filed.widget = form.TextInput(attrs={'placeholder' : field.label})

	class Meta:
		model = VoterCardPhotos
		fields = ('voterCardPhoto',)


class RartionCardForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(RartionCardForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			if field:
				if type(field.widget) in (forms.TextInput, forms.DateInput):
					filed.widget = form.TextInput(attrs={'placeholder' : field.label})

	class Meta:
		model = RationCardPhotos
		fields = ('rationCardPhoto',)

class PassPortForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PassPortForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			if field:
				if type(field.widget) in (forms.TextInput, forms.DateInput):
					filed.widget = form.TextInput(attrs={'placeholder' : field.label})

	class Meta:
		model = PassportPhotos
		fields = ('passportPhoto',)
