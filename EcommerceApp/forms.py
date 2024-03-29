from django import forms
from .models import Customer
    
class UserForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['name','email', 'address','phone']