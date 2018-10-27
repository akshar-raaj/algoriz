from django import forms

class AlgoForm(forms.Form):

    name = forms.CharField(max_length=100)
    signal = forms.CharField(max_length=1000)
    trade = forms.CharField(max_length=500)
    ticker = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(AlgoForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control '})
