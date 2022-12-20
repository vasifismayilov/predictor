from django import forms
from .models import Login_user
class LoginForm(forms.ModelForm):
    number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-field'
    }))
    class Meta:
        model = Login_user
        fields = '__all__'