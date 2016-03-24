import json

from django.test import TestCase, Client
from django.middleware import csrf


class MailTest(TestCase):
    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')

    def test_get_csrf_token(self):
        # testing that csrf token is returned on GET request to mail api
        response = self.client.get('/api/mail/send_mail/')
        request = response.wsgi_request
        csrf_token = csrf.get_token(request)

        self.assertEqual(json.loads(response.content.decode('utf8')), {'csrf_token': csrf_token})

    def test_send(self):
        response = self.client.post('/api/mail/send_mail/', {'to_address': 'noreply@openstax.org',
                                                             'from_name': 'Openstax',
                                                             'from_address': 'noreply@openstax.org',
                                                             'subject': 'Test Subject',
                                                             'message_body': 'This is a test.'})
        self.assertRedirects(response, '/contact-thank-you', target_status_code=301)