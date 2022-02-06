from django import forms


class MessageForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput({"placeholder": "Please enter your email"})
    )
    message = forms.CharField(
        widget=forms.Textarea({"placeholder": "Please enter your message"})
    )
