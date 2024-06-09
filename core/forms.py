from django import forms 
from .models import *
class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
        labels = {
            'name':'Book name',
            'author':'Author name',
        }
        error_messages={
            'name':{
                'required':"Enter book name"
            },
            'author':{
                'required':"Enter author name"
            }
        }
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name':'Author name'
        }
        error_messages={
            'name':{
                'required':"Enter book name"
            }
        }