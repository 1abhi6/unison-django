from django import forms


class formInput(forms.Form):
    name = forms.CharField(max_length=50, label="Name", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Input your name"}))
    contactNum = forms.IntegerField(label="Contact Number", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Input your Contact Number'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Input your email'}))
    message = forms.CharField(label="Your message", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Input your message'}))
