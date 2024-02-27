from django.db import models
class Links(models.Model):
    domainURL = models.URLField()

    domainTitle = models.CharField(max_length = 255)

    timeAccessed = models.CharField(max_length = 255)

    domainRating = models.PositiveIntegerField(default = 0)

    reasonNoHttps = models.BooleanField(default = False)
    reasonShortened = models.BooleanField(default = False)
    reasonAtSymbol = models.BooleanField(default = False)
    reasonBadExtension = models.BooleanField(default = False)

    clicked_count = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.domainURL