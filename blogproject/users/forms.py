from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
    
# class UserRegistrationForm(forms.Form):
    
#     username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     email = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows": 5}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
#     confirm = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UserRegistrationForm(UserCreationForm):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].label = "Enter your Username"
        self.fields["email"].label = "Enter your e-mail address"
        self.fields["password1"].label = "Enter your Password"
        self.fields["password2"].label = "Confirm your Password"
        
        self.fields["username"].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields["password1"].widget = forms.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = forms.PasswordInput(attrs={"class":"form-control"})



    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
    
# class LoginForm(forms.Form):
    
#     username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].label = "Enter your Username"
        self.fields["password"].label = "Enter your Password"
        
        self.fields["username"].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = forms.PasswordInput(attrs={"class":"form-control"})

    