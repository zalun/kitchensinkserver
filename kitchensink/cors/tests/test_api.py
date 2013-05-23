"""
collection.tests.test_api
-------------------------
"""
import logging
import simplejson

from nose.tools import eq_
from test_utils import TestCase

_log = logging.getLogger('kss.%s' % __name__)


class TestAPI(TestCase):
    def test_post_and_result(self):
        url = '/api/v1/cors/?format=json'
        post_response = self.client.post(url, content_type='application/json',
                                         data='{"message": "some message"}')
        eq_(post_response.status_code, 201)
        data = simplejson.loads(post_response.content)
        eq_(data['message'], 'some message')
