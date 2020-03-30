from django import forms

class ReportForm(forms.Form):
    textarea = forms.CharField(label="", widget=forms.Textarea)