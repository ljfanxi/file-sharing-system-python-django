from django import forms
from .models import RegTable, File

#First created Registration Form
class RegTableForm(forms.ModelForm):
    class Meta:
        model = RegTable
        fields = '__all__'
        
#Second created Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget = forms.PasswordInput)

#Third created Login Form
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
