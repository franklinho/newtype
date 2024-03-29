from django.db import models

# Create your models here.
class Intent(models.Model):
    idfa = models.CharField(max_length = 200)
    product_id = models.CharField(max_length = 200)
    advertiser_id = models.CharField(max_length = 200)
    converted = models.BooleanField(default=False)
    product_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __unicode__(self):
        return self.idfa

    def converted_lookup(self):
        return self.converted

class Product(models.Model):
    product_id = models.CharField(max_length = 200)
    product_name = models.CharField(max_length = 200)
    product_price = models.DecimalField(max_digits=12, decimal_places=2)
    advertiser_id = models.CharField(max_length = 200)
    product_image_url = models.CharField(max_length = 2000)
    product_url = models.CharField(max_length = 2000)
    def __unicode__(self):
        return self.product_name

class Element(models.Model):
    element_id = models.CharField(max_length = 200)
    element_type = models.CharField(max_length = 200)
    product_id = models.CharField(max_length = 200)
    text = models.CharField(max_length = 200)
    advertiser_id = models.CharField(max_length = 200)
    campaign_id = models.CharField(max_length = 200)
    impressions = models.IntegerField(default =0)
    clicks = models.IntegerField(default =0)
    conversions = models.IntegerField(default =0)
    def __unicode__(self):
        return self.element_id

class Click(models.Model):
    idfa = models.CharField(max_length = 200)
    advertiser_id = models.CharField(max_length = 200)
    product_id = models.CharField(max_length = 200)
    campaign_id = models.CharField(max_length = 200)
    converted = models.BooleanField(default=False)
    element_ids = models.CharField(max_length = 200)

class Campaign(models.Model):
    active = models.BooleanField(default=True)
    campaign_id = models.CharField(max_length = 200)
    advertiser_id = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    template = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.name