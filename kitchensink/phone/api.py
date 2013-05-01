"""
phone.api
---------
"""
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from kitchensink.phone.models import Phone


class PhoneResource(ModelResource):
    class Meta:
        queryset = Phone.objects.all()
        # there are only two methods allowed - ``get`` and ``post``
        # the phone may register once and doesn't change the id
        allowed_methods = ('get', 'post')
        authorization = Authorization()
        always_return_data = True
