from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from django import forms

class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=254, label='First Name')
    lastname = forms.CharField(max_length=254, label='Last Name')
    idnum = forms.CharField(max_length=254, label='ID Number')
    password1 = forms.CharField(max_length=254, label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=254, label='Password2', widget=forms.PasswordInput)

    def signup(self, request, user):
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.idnum = self.cleaned_data['idnum']
        print(request.user)
        print(request.user.is_authenticated)
        if(request.user.is_authenticated):
            print(request.user.is_administrator)
            if(request.user.is_administrator):
                user.is_manager = True
        user.save()

class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""
    renewal_date = forms.DateField(
            help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        # Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
