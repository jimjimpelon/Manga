from django.db import models
from django.utils import timezone
import datetime

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField('Date Searched')

    def __str__(self):
        return self.search

    def date_searched_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name_plural = "Searches"