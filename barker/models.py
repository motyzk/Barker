from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.core.urlresolvers import reverse


class Bark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='barks')
    content = models.CharField(max_length=141, validators=[MinLengthValidator(limit_value=1)])
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'user: {}\ncontent: {}\ndate: {}'.format(str(self.user), self.content, str(self.published_at))

    def get_absolute_url(self):
        return reverse("barker:detail_by_username", args=(self.user, ))


class MyUtil(models.Model):
    def urls_as_list(self):
        return self.screenshots.split('/')
