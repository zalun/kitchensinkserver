"""
collection.tests.test_api
-------------------------
"""
import logging
import simplejson

from nose.tools import eq_
from test_utils import TestCase

from kitchensink.device.models import Make, Device
from kitchensink.phone.models import Phone
from kitchensink.collection.models import Result

_log = logging.getLogger('kss.%s' % __name__)


class TestAPI(TestCase):
    def setUp(self):
        self.make = Make.objects.create(name='LG', slug='lg')
        self.device = Device.objects.create(make=self.make, model='Nexus4')
        # register the app in database
        self.phone = Phone.objects.create()

    def test_add_result(self):
        url = Result.get_api_uri('v1')
        test_result = {
            "device": self.device.get_resource_uri('v1'),
            "phone": self.phone.get_resource_uri('v1'),
            "user_agent": "user agent",
            "test_result": "test result"
        }

        post_response = self.client.post(url, content_type='application/json',
                                         data=simplejson.dumps(test_result))
        eq_(post_response.status_code, 201)
        eq_(Result.objects.count(), 1)
        eq_(self.device.results.count(), 1)
