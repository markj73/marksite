def errors_to_json(errors):
    """
    Convert a Form error list to JSON::
    """
    return dict(
            (k, map(unicode, v))
            for (k,v) in errors.iteritems()
        )

def set_date_input_formats(fields):
    """
    Helper to set the DateField input formats so that they accept finnish date format.
    """
    from django import forms
    for f in fields:
        if isinstance(fields[f], forms.DateField):
            # Use custom date field so that finnish date format is allowed when saving.
            fields[f].widget.format = '%d.%m.%Y'
            fields[f].input_formats = ['%d.%m.%Y']