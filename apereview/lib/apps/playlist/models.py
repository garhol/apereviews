from django.db import models
from tinymce import models as tinymce_models
from apereview.lib.apps.personnel.models import Personnel

from datetime import datetime

from django.db.models.signals import post_save, pre_save
import requests
from xml.etree.ElementTree import ElementTree
from xml.parsers.expat import ExpatError 
from xml.etree.ElementTree import fromstring

spotifyapi_url = "http://ws.spotify.com/search/1/track"

class Playlist(models.Model):
 
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('draft', 'Draft'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    playlist_url = models.CharField(max_length=255, default="http://www.apemanvinyl.com")
    playlist_image =  models.ImageField(upload_to='albums/images/%Y/%m/%d', null=True, blank=True)
    playlist_banner_image =  models.ImageField(upload_to='albums/images/banners/%Y/%m/%d', null=True, blank=True)
    content = tinymce_models.HTMLField()
    date_created = models.DateTimeField(auto_now_add = True, default=datetime.now)
    playlist_status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='Live')
    listauthor = models.ForeignKey(Personnel, related_name='listauthor')
    tags = models.TextField()

    def get_class(self):
        myclass = "playlist"
        return myclass


    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
		return "/playlists/%s" % self.slug
		
class PlaylistItem(models.Model):
    
    artist = models.CharField(max_length=255)
    track = models.CharField(max_length=255)
    spotifylink = models.CharField(max_length=255, null=True, blank=True)
    playlist = models.ForeignKey(Playlist)

    def __unicode__(self):
        return self.track


def pre_item_save(sender, instance, **kwargs):
    if not instance.spotifylink:
        try:
            data = {'q':instance.track}
            r = requests.get(spotifyapi_url, params=data)
            tree = fromstring(r.content)
            for node in tree.findall('.//{http://www.spotify.com/ns/music/1}track'):
                for album_name in node.findall('.//{http://www.spotify.com/ns/music/1}name'):
                    if album_name.text.lower() == instance.track.lower():
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

pre_save.connect(pre_item_save, sender=PlaylistItem)
