from django.db import models

class updatedLink(models.Model):
    domainURL = models.CharField(max_length = 255, default= "No-URL")

    domainTitle = models.CharField(max_length = 255, default= "No-Title")

    timeAccessed = models.CharField(max_length = 255, default= "Never happened")

    domainRating = models.IntegerField(default = 0)

    reasonNoHttps = models.BooleanField(default = False)
    reasonShortened = models.BooleanField(default = False)
    reasonAtSymbol = models.BooleanField(default = False)
    reasonBadExtension = models.BooleanField(default = False)
    reasonRedirect = models.BooleanField(default = False)
    reasonDashes = models.BooleanField(default = False)

    clicked_count = models.IntegerField(default = 1)

    def __str__(self):
        return self.domainURL
