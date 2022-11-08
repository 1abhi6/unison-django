from django import forms

# operChoices = [(1, '+'), (2, '-'), (3, '*'), (4, '/')]


class formInput(forms.Form):
    num = forms.CharField(label="Number", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder':'Input a number'}))
    # num2 = forms.CharField(label="Number 2", widget=forms.TextInput(
    #     attrs={'class': 'form-control'}))
    # oper = forms.CharField(label='Choose Operation',
    #                        widget=forms.Select(attrs={'class':'form-control'},choices=operChoices))
