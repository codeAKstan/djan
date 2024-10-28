from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    context = forms.CharField(required=False, widget=forms.Textarea)