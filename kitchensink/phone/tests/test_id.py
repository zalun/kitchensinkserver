"""
phone.tests.test_getid
----------------------
"""
import logging
import simplejson

from nose.tools import eq_
from test_utils import TestCase

from kitchensink.phone.models import Phone

_log = logging.getLogger('kss.%s' % __name__)


class TestId(TestCase):

    def test_create_and_return_id(self):
        url = Phone.get_api_uri('v1')
        create_response = self.client.post(url,
                                           content_type='application/json',
                                           follow=False)
        eq_(create_response.status_code, 201)
        eq_(Phone.objects.all().count(), 1)
        assert 'location' in create_response
        get_response = self.client.get(create_response['location'],
                                       content_type='application/json')
        data = simplejson.loads(get_response.content)
        assert 'error_message' not in data
        assert data['id']
