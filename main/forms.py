from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Your Name', 'style':"width:100%;"}),
            'email': forms.EmailInput(attrs={'placeholder':'Your Email Address', 'style':"width:100%;"}),
            'message': forms.Textarea(attrs={
                'placeholder':'How Can We Help?', 
                'style':"width:100%; height:170px; padding-top:17px; padding-bottom:17px; padding-left:27px; padding-right:27px;border: 1px solid #e6e6e6; border-radius: 2px;"}),
        }