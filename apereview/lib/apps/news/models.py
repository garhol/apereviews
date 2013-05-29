from django.db import models
from tinymce import models as tinymce_models
from apereview.lib.apps.personnel.models import Personnel

from datetime import datetime

class News(models.Model):
 
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('draft', 'Draft'),
    )

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)    
    promo_image =  models.ImageField(upload_to='news/images/%Y/%m/%d', null=True, blank=True)
    news_banner_image =  models.ImageField(upload_to='news/images/banners/%Y/%m/%d', null=True, blank=True)
    article = tinymce_models.HTMLField()
    date_created = models.DateTimeField(auto_now_add = True, default=datetime.now)
    news_status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='Live')
    reporter = models.ForeignKey(Personnel, related_name='reporter')
    tags = models.TextField()

    def __unicode__(self):
        return self.title
    
    def get_class(self):
        myclass = "news"
        return myclass
        
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        
