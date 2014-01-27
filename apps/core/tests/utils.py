from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.boards.models import Board

__author__ = 'petry'


class LoggedTestCase(TestCase):

    def setUp(self):
        super(LoggedTestCase, self).setUp()
        self.view = self.get_view()
        user = User.objects.create_superuser(
            username='test_user',
            email='test_email',
            password='test'
        )
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/some-url/')
        self.request.user = user
        self.request.session = {}

    def get_view(self):
        raise NotImplementedError()

    def assertRedirectIfNotLogged(self):
        self.request.user = AnonymousUser()
        self.response = self.view(self.request, pk=self.board.pk)
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response.url,
                         "{0}?next={1}".format(reverse('core-login'), '/some-url/'))