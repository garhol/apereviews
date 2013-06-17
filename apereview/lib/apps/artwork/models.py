from django.db import models
from tinymce import models as tinymce_models
from apereview.lib.apps.personnel.models import Personnel

from datetime import datetime

class ArtCollection(models.Model):
 
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('draft', 'Draft'),
    )
    
    title = models.CharField(max_length=255, help_text="The title of this collection")
    slug = models.CharField(max_length=255, help_text="Auto-generated from the title, overwrite if required")
    collection_image =  models.ImageField(upload_to='albums/images/%Y/%m/%d', null=True, blank=True, help_text="The pod image for this collection")
    content = tinymce_models.HTMLField(help_text="A small amount of text describing the collection")
    date_created = models.DateTimeField(auto_now_add = True, default=datetime.now)
    collection_status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='Live', help_text="Set to draft until you are sure you've checked everything :)")
    collection_author = models.ForeignKey(Personnel, related_name='artauthor', help_text="Set this collection to an author")
    tags = models.TextField(help_text="A list of relevant tags seperated by commas e.g 'images, black keys, album, art'")

    def get_class(self):
        myclass = "artcollection"
        return myclass

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
		return "/artwork/%s" % self.slug
        

class ArtItem(models.Model):
    
    artist = models.CharField(max_length=255, blank=True, help_text="The name of the original artist")
    artwork = models.ImageField(upload_to='albums/images/artwork/%Y/%m/%d', null=True, blank=True, help_text="Upload your piece of artwork")
    url = models.URLField(null=True, blank=True, help_text="Link for attribution")
    artcollection = models.ForeignKey(ArtCollection)

    def __unicode__(self):
        return self.artist
