from django.contrib.auth.models import User
from django.db import models
from tinymce import models as tinymce_models

class Personnel(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=255, help_text="Or full name")
    slug = models.CharField(max_length=255, help_text="Should autofill based on their name")
    job_title = models.CharField(max_length=255, help_text="What position does this individual hold")
    bio_pic =  models.ImageField(upload_to='writers/images/%Y/%m/%d', null=True, blank=True, help_text="Pod image")
    banner_image =  models.ImageField(upload_to='writers/images/banner/%Y/%m/%d', null=True, blank=True, help_text="Bio page image")
    biography = tinymce_models.HTMLField(help_text="Write something witty here")
    twitter_username = models.CharField(max_length=255, null=True, blank=True, help_text="Self promotion for writers")
    show_twitter_link = models.BooleanField(default=True, help_text="Works directly against the self promotion")

    def __unicode__(self):
        return self.nickname
        
    class Meta:
        verbose_name = "Writer"
        verbose_name_plural = "Writers"
