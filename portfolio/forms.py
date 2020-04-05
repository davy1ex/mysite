from django import forms

class FinalForm(forms.Form):
    login = forms.CharField(label='', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'first_name'})
     )
    
    password = forms.CharField(label='', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'last_name'})
     )

