from django.contrib.auth.models import User
from django.db import models
from tinymce import models as tinymce_models

class Personnel(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    job_title = models.CharField(max_length=255)
    bio_pic =  models.ImageField(upload_to='writers/images/%Y/%m/%d', null=True, blank=True)
    banner_image =  models.ImageField(upload_to='writers/images/banner/%Y/%m/%d', null=True, blank=True)
    biography = tinymce_models.HTMLField()
    twitter_username = models.CharField(max_length=255, null=True, blank=True)
    show_twitter_link = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nickname
        
    class Meta:
        verbose_name = "Writer"
        verbose_name_plural = "Writers"
