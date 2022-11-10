from django.forms import ModelForm
from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import Comment


class CommentForm(ModelForm):        
    class Meta: 
        model = Comment
        fields = ['first_name', 'last_name', 'comment',]
        labels = {
            'first_name': '','last_name': '', 'comment': ''
        }
        widgets = {
        'first_name': TextInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'First Name'
            }),
        
        'last_name': TextInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Last Name'
            }),

        'comment': Textarea(attrs={
            'class': "form-control",
            'style': 'max-width: 600px;',
            'rows':5,
            'placeholder': 'Type Comment here'
            }),
        }
