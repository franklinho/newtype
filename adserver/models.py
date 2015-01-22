from django.db import models

# Create your models here.
class Intent(models.Model):
    idfa = models.CharField(max_length = 200)
    product_id = models.CharField(max_length = 200)
    advertiser_id = models.CharField(max_length = 200)
    converted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.idfa

    def converted_lookup(self):
        return self.converted


class Element(models.Model):
    element_id = models.CharField(max_length = 200)
    element_type = models.CharField(max_length = 200)
    product_id = models.CharField(max_length = 200)
    advertiser_id = models.CharField(max_length = 200)
    campaign_id = models.CharField(max_length = 200)
    impressions = models.IntegerField(default =0)
    clicks = models.IntegerField(default =0)
    conversions = models.IntegerField(default =0)
    # def __unicode__(self):              # __unicode__ on Python 2
     #    return self.element_id

class Click(models.Model):
    idfa = models.CharField(max_length = 200)
    advertiser_id = models.CharField(max_length = 200)
    product_id = models.CharField(max_length = 200)
    campaign_id = models.CharField(max_length = 200)
    converted = models.BooleanField(default=False)
    element_ids = models.CharField(max_length = 200)
    # def __unicode__(self):              # __unicode__ on Python 2
        # return self.idfa