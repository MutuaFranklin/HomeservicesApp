from . models import Profile, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
      
        def __init__(self, *args, **kwargs):
            super(UserRegistrationForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None

        fields = ('first_name', 'last_name', 'email','username',  'password1', 'password2')
        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.PasswordInput(attrs = {'class':'form-control ', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.PasswordInput(attrs = {'class':'form-control', 'type':'password', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profile_pic', 'mobile', 'gender','bio', 'home_location', 'main_service', 'secondary_service_one', 'secondary_service_two']
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            'bio':forms.Textarea(attrs={'class': 'form-control'}),
            'home_location':forms.TextInput(attrs={'class': 'form-control'}),
            # 'current_location':forms.TextInput(attrs={'class': 'form-control'}),
            'main_service':forms.Select(attrs={'class': 'form-control'}),
            'secondary_service_one':forms.Select(attrs={'class': 'form-control'}),
            'secondary_service_two':forms.Select(attrs={'class': 'form-control'}),
            
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('service', 'task_description', 'review', 'rating')
        widgets = {
            'service':forms.Select(attrs={'class': 'form-control'}),
            'task_description':forms.TextInput(attrs={'class': 'form-control'}),
            'review':forms.Textarea(attrs={'class': 'form-control'}),
            'rating':forms.Select(attrs={'class': 'form-control'}),
        }




