from django.core.exceptions import ValidationError
from django.test import TestCase
import string
import random
from django.contrib.auth.models import User
from . import models


class BarksTestCase(TestCase):
    def test_barks(self):
        users = [User.objects.create_user(
            "user #{}".format(i + 1)) for i in range(3)]
        n = 8
        for i in range(n):
            chars_num = random.randint(0, 141)
            b = models.Bark(
                user=random.choice(users),
                content=''.join(random.choice(string.ascii_letters + string.digits) for i in range(chars_num)),
            )
            b.full_clean()
            b.save()
        self.assertEquals(models.Bark.objects.count(), n)

    def test_empty_bark(self):
        '''the minimum number of characters a bark is 1. this test checks
        that a validation error is raised when trying to generate an empty bark'''
        b = models.Bark(
            user=User.objects.create_user('user'),
            content='',
        )
        with self.assertRaises(ValidationError):
            b.full_clean()
        b.save()

    def test_user_page(self):
        u = User.objects.create_user('moshe')
        b = models.Bark(
            user=u,
            content='my first bark',
        )
        b.save()
        url = '/moshe/'
        resp=self.client.get(url)
        self.assertContains(resp, b.content)
