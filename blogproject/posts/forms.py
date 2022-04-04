from django import forms
from .models import Post

# class PostCreationForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     content = forms.CharField(max_length=50)
#     author = forms.CharField(max_length=50)
    
    
class PostCreationForm(forms.ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows": 5}))
    author = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    
    class Meta:
        model = Post
        fields = '__all__'