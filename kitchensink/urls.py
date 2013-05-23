from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from funfactory.monkeypatches import patch
from tastypie.api import Api

from phone.api import PhoneResource
from device.api import MakeResource, DeviceResource
from collection.api import ResultResource
from cors.api import CORSResource

patch()
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PhoneResource())
v1_api.register(MakeResource())
v1_api.register(DeviceResource())
v1_api.register(ResultResource())
v1_api.register(CORSResource())

urlpatterns = patterns('',
    # Generate a robots.txt
    (r'^robots\.txt$',
        lambda r: HttpResponse(
            "User-agent: *\n%s: /" % 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow' ,
            mimetype="text/plain"
        )
    ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^api/', include(v1_api.urls)),
    (r'^admin/', include(admin.site.urls)),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
