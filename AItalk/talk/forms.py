from django import forms


class ChatForm(forms.Form):
    message = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"size": "80%"}))
