from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        blank=True,
        upload_to='images/'
    )
    thumb_img = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 150)],
        format='JPEG',
        options={
            'quality': 90,
        }
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title