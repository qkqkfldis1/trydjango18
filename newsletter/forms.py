from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
        extensions = ["ac.kr", "com", "net", "go.kr", "co.kr"]
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain = provider.split('.')[0]
        extension = provider.split('.')[1:]
        # print(domain, extension)
        if len(extension) == 2:
            extension = extension[0] + "." + extension[1]
            # print(extension)
        # if not domain == 'kaist':
        #     raise forms.ValidationError("Please make sure use kaist mail")
        if not extension in extensions:
            raise forms.ValidationError("Please use a vaild email address")
        return email

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        # exclude = ['full_name']

    def clean_email(self):
        extensions = ["ac.kr", "com", "net", "go.kr", "co.kr"]
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain = provider.split('.')[0]
        extension = provider.split('.')[1:]
        # print(domain, extension)
        if len(extension) == 2:
            extension = extension[0] + "." + extension[1]
            # print(extension)
        # if not domain == 'kaist':
        #     raise forms.ValidationError("Please make sure use kaist mail")
        if not extension in extensions:
            raise forms.ValidationError("Please use a vaild email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # write validation code.
        return full_name
