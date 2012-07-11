from django.views.generic.base import *
from django.views.generic.edit import *
from django.utils import simplejson as json
from django.utils.translation import ugettext as _
from django.http import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import *

from custom.forms import errors_to_json
from custom.utils.simplejson import *
from modules.customer.decorators import *

class MixedTemplateView(TemplateView):
    """
    Custom template view that speaks JSON
    """
    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response with a template rendered with the given context.
        """
        self.message = _("Success")
        self.data = context
        self.success = True

        payload = {'success': self.success, 'message': self.message, 'data':self.data}

        if self.request.is_ajax():
            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )

        else:
            return super(MixedTemplateView, self).render_to_response(
                context, **response_kwargs
            )


class MixedFormView(FormView):
    """
    Custom form view that speaks JSON
    """
    def form_valid(self, form, *args, **kwargs):
        """
        The Form is valid
        """
        if self.request.is_ajax():
            self.message = _("Validation passed. Form Saved.")
            self.data = None
            self.success = True

            payload = {'success': self.success, 'message': self.message, 'data':self.data}

            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )
        else:
            return HttpResponseRedirect(
                self.get_success_url()
            )

    def form_invalid(self, form, *args, **kwargs):
        """
        The Form is invalid
        """
        #form.save()

        self.message = _("Validation failed.")
        self.data = errors_to_json(form.errors)
        self.success = False

        payload = {'success': self.success, 'message': self.message, 'data':self.data}

        if self.request.is_ajax():
            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )
        else:
            return super(MixedFormView, self).form_invalid(
                form, *args, **kwargs
            )

class GiosgTemplateView(MixedTemplateView):
    """
    Base giosg template view. 
    'speaks' HTML and JSON.
    requires caller to be logged in
    """
    template_name = 'dw/report.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """
        The Dispatcher
        """
        return super(GiosgTemplateView, self).dispatch(*args, **kwargs)

class GiosgManagerTemplateView(MixedTemplateView):
    """
    Base giosg template view. 
    'speaks' HTML and JSON.
    requires caller to be logged in
    """
    template_name = 'dw/report.html'

    @method_decorator(login_required)
    @method_decorator(only_managers_allowed)
    def dispatch(self, *args, **kwargs):
        """
        The Dispatcher
        """
        return super(GiosgManagerTemplateView, self).dispatch(*args, **kwargs)

