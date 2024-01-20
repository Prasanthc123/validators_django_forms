from django import forms
#from django.core import validators

def sname_validation(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('started with a')

def sname_len_validation(data):
    if len(data)<5:
        raise forms.ValidationError('length is less then 5')

class Schoolform(forms.Form):
    sname=forms.CharField(validators=[sname_validation,sname_len_validation])
    sprincipal=forms.CharField()
    slocation=forms.CharField()
    semail=forms.EmailField()
    remail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)
    def clean(self):
        e=self.cleaned_data['semail']
        re=self.cleaned_data['remail']

        if e!=re:
            raise forms.ValidationError('email not match')
    
    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bot')