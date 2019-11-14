from django.db import models


# Just a raw SQL request passed through this model.
# Should be removed before production version.
class Request(models.Model):
    query = models.TextField()
