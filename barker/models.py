from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models


class Bark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='barks')
    content = models.CharField(max_length=141, validators=[MinLengthValidator(limit_value=1)])
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'user: {}\ncontent: {}\ndate: {}'.format(self.content, str(self.user), str(self.published_at))
