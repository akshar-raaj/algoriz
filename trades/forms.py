from django import forms

class AlgoForm(forms.Form):

    name = forms.CharField(max_length=100)
    signal = forms.CharField(max_length=1000)
    trade = forms.CharField(max_length=500)
    ticker = forms.CharField(max_length=100)
