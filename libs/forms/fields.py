import re
from datetime import date
from calendar import monthrange

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from widgets import *

class CreditCardField(forms.CharField):
    """
    Form field that validates credit card numbers.
    """
    CREDIT_CARD_RE = r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\d{11})$'

    widget = forms.TextInput(attrs={'maxlength': 19})

    default_error_messages = {
        'required': _(u'This field is required.'),
        'invalid': _(u'The credit card number you entered is invalid.'),
    }

    def clean(self, value):
        """
        Clean method.
        """
        if value is not None:
            value = value.replace(' ', '').replace('-', '')

        if self.required and not value:
            raise forms.util.ValidationError(self.error_messages['required'])
        if value and not re.match(self.CREDIT_CARD_RE, value):
            raise forms.util.ValidationError(self.error_messages['invalid'])
        return value


class ExpiryDateField(forms.MultiValueField):
    """
    Form field that validates credit card expiry dates.
    """
    default_error_messages = {
        'invalid_year': _(u'Please enter a valid year.'),
        'invalid_month': _(u'Please enter a valid month.'),
        'date_passed': _(u'This expiry date has passed.'),
    }

    def __init__(self, *args, **kwargs):
        """
        Initializer
        """
        if 'initial' not in kwargs:
            kwargs['initial'] = date.today()

        fields = (
            forms.ChoiceField(choices=[(x, '%02d' % x) for x in range(1, 13)],
                error_messages={'invalid': self.default_error_messages['invalid_month']}),
            forms.ChoiceField(choices=[(x, x) for x in range(date.today().year, 2025)],
                error_messages={'invalid': self.default_error_messages['invalid_year']}),
        )

        #Initialize the field and the custom widget
        super(ExpiryDateField, self).__init__(fields, *args, **kwargs)
        self.widget = ExpiryDateWidget(widgets=[fields[0].widget, fields[1].widget])

    def clean(self, value):
        """
        Clean method. (Check whether the date has passed/expired.)
        """
        expiry_date = super(ExpiryDateField, self).clean(value)

        if date.today() > expiry_date:
            raise forms.ValidationError(self.error_messages['date_passed'])
        else:
            return expiry_date

    def compress(self, data_list):
        """
        Compressor
        """
        if data_list:
            month, year = [int(x) for x in data_list]
            if year in range(date.today().year, 2025) and month in range(13):
                  return date(year, month, monthrange(year, month)[1])
            else:
                raise forms.ValidationError(self.error_messages['invalid_date'])
        else:
            return None


class VerificationValueField(forms.CharField):
    """
    Form field that validates credit card verification values (e.g. CVV2).
    """
    VERIFICATION_VALUE_RE = r'^([0-9]{3,4})$'

    widget = forms.TextInput(attrs={'maxlength': 4})

    default_error_messages = {
        'required': _(u'This field is required.'),
        'invalid': _(u'The verification value you entered is invalid.'),
    }

    def clean(self, value):
        """
        Clean method.
        """
        if value is not None:
            value = value.replace(' ', '').replace('-', '')

        if not value and self.required:
            raise forms.util.ValidationError(self.error_messages['required'])
        if value and not re.match(self.VERIFICATION_VALUE_RE, value):
            raise forms.util.ValidationError(self.error_messages['invalid'])
        return value


class ConfirmPasswordField(forms.MultiValueField):
    """
    Form field that validates that two passwords are the same.
    """
    default_error_messages = {
        'password_no_match': _(u'The two passwords don\'t match.'),
        'short_password': _(u'The password is too short.'),
        'invalid_password': _(u'The password is invalid.'),
    }

    def __init__(self, *args, **kwargs):
        """
        Initializer
        """
        if 'initial' not in kwargs:
            kwargs['initial'] = ''

        #Yah
        #pass1
        #pass2

        fields = (
            forms.CharField(widget=forms.PasswordInput,
                error_messages={'invalid': self.default_error_messages['invalid_password']}),
            forms.CharField(widget=forms.PasswordInput,
                error_messages={'invalid': self.default_error_messages['invalid_password']}),
        )

        #Initialize the field and the custom widget
        super(ConfirmPasswordField, self).__init__(fields, *args, **kwargs)
        self.widget = ConfirmPasswordWidget(widgets=[fields[0].widget, fields[1].widget])

    def clean(self, value):
        """
        Clean method. (Check whether the password is too short.)
        """
        password = super(ConfirmPasswordField, self).clean(value)

        if len(password) < 8:
            raise forms.ValidationError(self.error_messages['short_password'])
        else:
            return password

    def compress(self, data_list):
        """
        Compressor
        """
        if data_list:
            password1, password2 = data_list
            if password1 == password2:
                return password1
            else:
                raise forms.ValidationError(self.error_messages['password_no_match'])
        else:
            return None
