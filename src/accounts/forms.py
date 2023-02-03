from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser

from django import forms


"""
This code defines a UserRegistrationForm class that extends Django's UserCreationForm. It adds an email field and a firstname field, both with custom error messages for the required validation. The Meta class sets the model to the custom CustomUser model and the fields to be used for registration as email and firstname. The form also includes a captcha field using the ReCaptchaField widget. The clean_email method checks if the email already exists in the CustomUser model, and raises a validation error if it does. The clean_firstname method cleans the entered first name by stripping whitespaces and converting it to title case.
"""
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(error_messages={'required': 'This field is required.'})
    firstname = forms.CharField(error_messages={'required': 'This field is required.'}, max_length=30)

    class Meta:
        model = CustomUser
        fields = ('email', 'firstname')

    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Please enter another email address.')
        return email

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname'].strip().title()
        return firstname
    
    

"""
This code defines a LoginForm class that extends Django's AuthenticationForm. It specifies an error message to display if the login fails and sets the model attribute to the custom CustomUser model. The form also includes a captcha field using the ReCaptchaField widget. The clean_username method is implemented to clean the entered username by converting it to lowercase and stripping whitespaces. It also raises a validation error if the email doesn't match any existing CustomUser email.
"""
class LoginForm(AuthenticationForm):
    
    error_messages = {'invalid_login': ('an error has occurred, please try again'),}
    
    model = CustomUser
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower().strip()
        if not CustomUser.objects.filter(email=username).exists():
            raise ValidationError('Please enter a correct email address.')
        return username