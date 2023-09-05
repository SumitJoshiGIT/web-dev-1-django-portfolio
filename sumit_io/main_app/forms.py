
from django.forms import ModelForm
from .models import Messages
from django import forms
class MessageForm(ModelForm):
    class Meta:
        model=Messages
        fields="__all__"
        labels={
            "name": "Name",
            "email": "Email",
            "message": "Message",
        }
        widgets={
            "name": forms.TextInput(attrs={"placeholder": "Name..."}),
            "email": forms.EmailInput(attrs={"placeholder": "Email..."}),
            "message": forms.Textarea(attrs={"placeholder": "Message..."}),
        }

class MessageForm2(forms.Form):       
    name=forms.CharField(label="Your Name",widget=forms.TextInput(attrs={"placeholder":"Enter your name...."}),max_length=30,min_length=4)
    email=forms.EmailField(label="Email:",max_length=50, required=False,widget=forms.TextInput(attrs={"placeholder":"Enter your email...."}))
    message=forms.CharField(widget=forms.Textarea(attrs={"name":"message","placeholder":"Enter your message"}))
