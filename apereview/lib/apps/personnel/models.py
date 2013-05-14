from django.contrib.auth.models import User
from django.db import models

class Personnel(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nickname
