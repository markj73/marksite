from django.views.generic.edit import *
from django.views.generic.list import *
from django.views.generic.detail import *
from django.utils import simplejson as json
from django.utils.translation import ugettext as _
from django.http import *
from django.forms.models import model_to_dict
from django.db import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import *

from libs.forms import errors_to_json
from libs.utils.simplejson import *

class HybridDetailView(DetailView):
    """
    Custom detail generic view that speaks JSON
    """
    def get(self, request, *args, **kwargs):
        """
        The GET method
        """
        self.object = self.get_object()

        self.message = _("Success")

        if isinstance(self.object, models.Model):
            self.data = model_to_dict(self.object)
        else:
            self.data = self.object
        self.success = True

        payload = {'success': self.success, 'message': self.message, 'data':self.data}

        if self.request.is_ajax():
            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )

        else:
            return super(HybridDetailView, self).get(
                request, *args, **kwargs
            )

class HybridCreateView(CreateView):
    """
    Custom create generic view that speaks JSON
    """
    def form_valid(self, form, *args, **kwargs):
        """
        The Form is valid
        """
        #self.object = form.save()
        
        if self.request.is_ajax():
            self.message = _("Validation passed. Form Saved.")
            try:
                d = self.data
            except AttributeError:
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

        if self.request.is_ajax():
            self.message = _("Validation failed.")
            self.data = errors_to_json(form.errors)
            self.success = False

            payload = {'success': self.success, 'message': self.message, 'data':self.data}

            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )

class HybridFormView(FormView):
    """
    Custom form generic view that speaks JSON
    """
    def form_valid(self, form, *args, **kwargs):
        """
        The Form is valid
        """
        if self.request.is_ajax():
            self.object = self.get_object()
            self.message = _("Success")
            if isinstance(self.object, models.Model):
                self.data = model_to_dict(self.object)
            else:
                self.data = self.object
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
        if self.request.is_ajax():
            self.message = _("Validation failed.")
            self.data = errors_to_json(form.errors)
            self.success = False

            payload = {'success': self.success, 'message': self.message, 'data':self.data}

            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )

class HybridDeleteView(DeleteView):
    """
    Custom delete generic view that speaks JSON
    """
    def post(self, request, *args, **kwargs):
        """
        The POST method
        """
        self.get_object().delete()

        if self.request.is_ajax():
            self.message = _("Success")
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

class HybridUpdateView(UpdateView):
    """
    Custom update generic view that speaks JSON
    """
    def form_valid(self, form, *args, **kwargs):
        """
        The Form is valid
        """
        #self.object = form.save()

        if self.request.is_ajax():
            self.message = _("Validation passed. Form Saved.")
            try:
                d = self.data
            except AttributeError:
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
        if self.request.is_ajax():
            self.message = _("Validation failed.")
            self.data = errors_to_json(form.errors)
            self.success = False

            payload = {'success': self.success, 'message': self.message, 'data':self.data}

            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )


    def get(self, request, *args, **kwargs):
        """
        The GET method
        """
        self.object = self.get_object()

        if self.request.is_ajax():
            self.message = _("Success")
            if isinstance(self.object, models.Model):
                self.data = model_to_dict(self.object)
            else:
                self.data = self.object
            self.success = True

            payload = {'success': self.success, 'message': self.message, 'data':self.data}

            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )

        else:
            return super(HybridUpdateView, self).get(
                request, *args, **kwargs
            )

class HybridListView(ListView):
    """
    Custom manage generic view that speaks JSON
    """
    def get(self, request, *args, **kwargs):
        """
        The GET method
        """

        if self.request.is_ajax():
            self.object_list = self.get_queryset()
            self.message = _("Success")

            self.data = []
            for obj in self.object_list:
                if isinstance(obj, models.Model):
                    self.data.append(model_to_dict(obj))
                else:
                    self.data.append(obj)

            #self.data = [model_to_dict(object) for object in self.object_list]
            self.success = True

            payload = {'success': self.success, 'message': self.message, 'data':self.data}

            return HttpResponse(json.dumps(payload, default=encode_datetime),
                content_type='application/json',
            )

        else:
            return super(HybridListView, self).get(
                request, *args, **kwargs
            )

class LoginHybridDetailView(HybridDetailView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginHybridDetailView, self).dispatch(*args, **kwargs)

class LoginHybridCreateView(HybridCreateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginHybridCreateView, self).dispatch(*args, **kwargs)

class LoginHybridDeleteView(HybridDeleteView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginHybridDeleteView, self).dispatch(*args, **kwargs)

class LoginHybridUpdateView(HybridUpdateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginHybridUpdateView, self).dispatch(*args, **kwargs)

class LoginHybridListView(HybridListView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginHybridListView, self).dispatch(*args, **kwargs)

