from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name',    # To show perticular fields of the table
        'email', 'username', 'password']

        # excludes = ['']                         To select only those not in excludes

        label = {
            'password': 'password'
        }

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.                
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None

        forms.ModelForm.__init__(self, *args, **kwargs)

    # def clean_email(self):
    #     if self.cleaned_data['email'].endsWith('@gmail.com'):       # Email Validation
    #         return self.cleaned_data['email']
    #     else:
    #         return ValidationError("Email id is not valid")
    
    def save(self):
        password = self.cleaned_data.pop('password')
        role = self.cleaned_data.pop('role')
        u = super().save()
        u.groups.set([role])
        u.set_password(password)
        u.save()
        return u
