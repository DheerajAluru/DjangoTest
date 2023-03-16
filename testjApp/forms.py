from django import forms
from .models import userProfileModel
 
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userProfileModel
        fields = ['owner',
        'Name',
        'Date_of_birth',
        'Gender',
        'Image'
        ]