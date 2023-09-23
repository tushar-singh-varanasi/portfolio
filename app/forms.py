from django import forms

from app.models import contact

class Contact(forms.ModelForm):
    class Meta:
        model = contact
        fields = ("Name","Email","message")
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'})


            
        }
       
