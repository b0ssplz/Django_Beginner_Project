from django import forms
    
class UserRegistrationForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows": 5}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    
class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
