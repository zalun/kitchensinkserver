"""
cors.api
----------
"""
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.resources import Resource


class CORSObject(object):
    uuid = None
    message = None

    def __init__(self, initial=None):
        self.uuid = 1


class CORSResource(Resource):
    """This resourse is not saving a thing. It is used only to provide valid
    CORS answer
    """
    message = fields.CharField(attribute='message')

    class Meta:
        resource_name = 'cors'
        authorization = Authorization()
        allowed_methods = ('post', )
        object_class = CORSObject
        always_return_data = True

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.uuid
        else:
            kwargs['pk'] = bundle_or_obj.uuid

        return kwargs

    def obj_create(self, bundle, request=None, **kwargs):
        bundle.obj = CORSObject()
        bundle = self.full_hydrate(bundle)
        return bundle
