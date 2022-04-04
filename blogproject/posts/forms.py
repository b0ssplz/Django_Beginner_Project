from django import forms


class PostCreationForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    
    
    