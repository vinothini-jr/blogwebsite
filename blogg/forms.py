from django import forms
from .models import Comment, register
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=("name","body")

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "body":forms.Textarea(attrs={"class":"form-control"}),
        }
class RegisterForm(forms.ModelForm):
    class Meta:
        model=register
        fields=["name","email"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.Textarea(attrs={"class": "form-control"}),
        }