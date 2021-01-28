from django.db import models


# Create your models here.
class CheckLinksResult(models.Model):
    check_date = models.DateField(auto_now=True)
    original_link_url = models.CharField(max_length=250)
    history = models.CharField(max_length=250)
    final_link_url = models.CharField(max_length=250)
    final_link_status = models.CharField(max_length=250)

    def __str__(self):
        return self.original_link_url
