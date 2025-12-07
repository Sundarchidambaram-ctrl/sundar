from django import forms

# Example form
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
