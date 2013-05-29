from django.db import models
from tinymce import models as tinymce_models
from apereview.lib.apps.personnel.models import Personnel

from datetime import datetime

class Review(models.Model):

    APE_SCORE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
 
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('draft', 'Draft'),
    )

    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    label = models.CharField(max_length=255, default="Apeman")
    album_image =  models.ImageField(upload_to='albums/images/%Y/%m/%d', null=True, blank=True)
    album_banner_image =  models.ImageField(upload_to='albums/images/banners/%Y/%m/%d', null=True, blank=True)
    review = tinymce_models.HTMLField()
    date_created = models.DateTimeField(auto_now_add = True, default=datetime.now)
    score = models.CharField(
        max_length=15, choices=APE_SCORE, default='1')
    review_status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='Live')
    release_date = models.DateField(null=True)
    reviewer = models.ForeignKey(Personnel, related_name='reviewer')
    tags = models.TextField()


    def get_class(self):
        myclass = "review"
        return myclass


    def __unicode__(self):
        return self.album
