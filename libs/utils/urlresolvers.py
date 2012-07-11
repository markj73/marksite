from django.utils.functional import lazy
from django.core.urlresolvers import reverse

reverse_lazy = lazy(reverse, unicode) 