from django import forms
import datetime

class ExpiryDateWidget(forms.MultiWidget):
    """
    Widget containing two select boxes for selecting the month and year.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializer
        """
        super(ExpiryDateWidget, self).__init__(*args, **kwargs)

    def decompress(self, value):
        """
        Decompressor
        """
        return [value.month, value.year] if value else [None, None]

    def format_output(self, rendered_widgets):
        """
        Renders the HTML of the widget
        """
        return u'<div class="expirydatefield">%s</div>' % ' '.join(rendered_widgets)


class ConfirmPasswordWidget(forms.MultiWidget):
    """
    Form field which prompts the user to type in his password twice.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializer
        """
        super(ConfirmPasswordWidget, self).__init__(*args, **kwargs)

    def decompress(self, value):
        """
        Decompressor
        """
        return [value, value] if value else [None, None]

    def format_output(self, rendered_widgets):
        """
        Renders the HTML of the widget
        """
        return u'<div class="expirydatefield">%s</div>' % '<br />'.join(rendered_widgets)
    
    
