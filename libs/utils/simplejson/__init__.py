import datetime

from django.db.models.fields.files import *

def encode_datetime(obj):
    """
    Extended encoder function that helps to serialize dates and images
    """
    
    if isinstance(obj, datetime.datetime):
        try:
            return obj.strftime('%d.%m.%Y %H:%M:%S')
        except ValueError, e:
            return ''
    
    if isinstance(obj, datetime.date):
        try:
            return obj.strftime('%d.%m.%Y')
        except ValueError, e:
            return ''

    if isinstance(obj, ImageFieldFile):
        try:
            return obj.url
        except ValueError, e:
            return ''

    raise TypeError(repr(obj) + " is not JSON serializable. Type \"" + str(type(obj)) + "\" not supported!")