"""
collection.api
--------------
"""
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from kitchensink.device.api import DeviceResource
from kitchensink.phone.api import PhoneResource
from kitchensink.collection.models import Result


class ResultResource(ModelResource):
    device = fields.ForeignKey(DeviceResource, 'device', null=True)
    phone = fields.ForeignKey(PhoneResource, 'phone')

    class Meta:
        queryset = Result.objects.all()
        allowed_methods = ('get', 'post')
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'device': ALL_WITH_RELATIONS,
            'phone': ALL_WITH_RELATIONS
        }
