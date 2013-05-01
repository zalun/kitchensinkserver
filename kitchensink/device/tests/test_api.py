"""
phone.tests.test_getid
----------------------
"""
import logging
import simplejson

from nose.tools import eq_
from test_utils import TestCase

from kitchensink.device.models import Make, Device

_log = logging.getLogger('kss.%s' % __name__)


class TestAPI(TestCase):

    def setUp(self):
        self.lg = Make.objects.create(name='LG', slug='lg')
        self.nexus = Device.objects.create(make=self.lg, model='Nexus4')

    def test_get_makes(self):
        url = Make.get_api_uri('v1')
        response = self.client.get(url, content_type='application/json')
        eq_(response.status_code, 200)
        data = simplejson.loads(response.content)
        eq_(len(data['objects']), 1)
        eq_(data['objects'][0]['name'], self.lg.name)

    def test_get_devices_for_make(self):
        url = '%s?make__slug=%s' % (Device.get_api_uri('v1'), self.lg.slug)
        response = self.client.get(url, content_type='application/json')
        eq_(response.status_code, 200)
        data = simplejson.loads(response.content)
        eq_(len(data['objects']), 1)
        eq_(data['objects'][0]['make']['name'], self.lg.name)
        eq_(data['objects'][0]['model'], self.nexus.model)
