from django.db import models

class Athlete(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    birthday = models.DateField()
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    
# Create your models here.
