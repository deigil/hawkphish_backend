from django.db import models
class Links(models.Model):
    
    domainURL = models.CharField(max_length = 255)
    domainTitle = models.CharField(max_length = 255)
    timeAccessed = models.CharField(max_length = 255)
    domainRating = models.IntegerField()
    reasonNoHttps = models.BooleanField(default = False)
    reasonShortened = models.BooleanField(default = False)
    reasonAtSymbol = models.BooleanField(default = False)
    reasonBadExtension = models.BooleanField(default = False)
    clicked_count = models.IntegerField(default = 1)

    def __str__(self):
        return self.domainURL

