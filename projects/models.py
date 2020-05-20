import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=150)
    details = models.CharField(max_length=350)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    def is_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
