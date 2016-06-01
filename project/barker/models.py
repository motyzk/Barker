from django.conf import settings
from django.db import models


class Bark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='barks')
    content = models.CharField(max_length=141) #add min_length=1
    pub_date = models.DateField()

    def __str__(self):
        return 'content: {}'.format(self.content)