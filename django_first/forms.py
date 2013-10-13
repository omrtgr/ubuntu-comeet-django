from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	#Django prepares the html automatically.
	#email = forms.EmailField(required=True)
	#home_phone = forms.home_phone(required=True)
	
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email', 'password1','password2')

	def save(self,commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		#user.home_phone = self.cleaned_data['home_phone']
				

		if commit:
			user.save()
		return user
