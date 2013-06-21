from django.db import models
from tinymce import models as tinymce_models
from apereview.lib.apps.personnel.models import Personnel

from datetime import datetime

from django.db.models.signals import post_save, pre_save
import requests
from xml.etree.ElementTree import ElementTree
from xml.parsers.expat import ExpatError 
from xml.etree.ElementTree import fromstring


spotifyapi_url = "http://ws.spotify.com/search/1/album"

class Review(models.Model):

    APE_SCORE = (
        ('1', '0.5'),
        ('2', '1'),
        ('3', '1.5'),
        ('4', '2'),
        ('5', '2.5'),
        ('6', '3'),
        ('7', '3.5'),
        ('8', '4'),
        ('9', '4.5'),
        ('10', '5'),
    )
 
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('draft', 'Draft'),
    )

    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    spotifylink = models.CharField(max_length=255, null=True, blank=True)
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
        
    def get_absolute_url(self):
		return "/reviews/%s" % self.slug


def pre_rev_save(sender, instance, **kwargs):
    if not instance.spotifylink:
        try:
            data = {'q':instance.album}
            r = requests.get(spotifyapi_url, params=data)
            tree = fromstring(r.content.encode('utf-8'))
            for node in tree.findall('.//{http://www.spotify.com/ns/music/1}album'):
                for album_name in node.findall('.//{http://www.spotify.com/ns/music/1}name'):
                    if album_name.text.lower() == instance.album.lower():
                        album = album_name.text
                        for artist_name in node.findall('.//{http://www.spotify.com/ns/music/1}artist'):
                            art = artist_name.find('.//{http://www.spotify.com/ns/music/1}name')
                            if art.text.lower() == instance.artist.lower():
                                artist = art.text
                                href = node.attrib.get('href')
                                instance.spotifylink = href
                                break
        except:
            pass
	
pre_save.connect(pre_rev_save, sender=Review)
