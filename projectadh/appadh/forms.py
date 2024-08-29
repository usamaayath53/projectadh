from.models import newApplication
from django import forms

class newappForm(forms.ModelForm):
    class Meta:
        model=newApplication
        fields='__all__'
    

