from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

__author__ = 'petry'


class ProtectedViewMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProtectedViewMixin, self).dispatch(request, *args, **kwargs)