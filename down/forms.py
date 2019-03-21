from django import forms

class ContactForm(forms.Form):
    url = forms.CharField(max_length=3000)
    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     message = cleaned_data.get('message')
    #     if not name and not email and not message:
    #         raise forms.ValidationError('You have to write something!')