from django.db import models

from django.db import models
from tinymce import models as tinymce_models

class AboutText(models.Model):
   
    content = tinymce_models.HTMLField()

    def __unicode__(self):
        return "About us content"
        
    class Meta:
        verbose_name = "About text"
        verbose_name_plural = "About text"
