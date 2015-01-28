from django.contrib import admin
from adserver.models import Intent,Click, Product, Element, Campaign
# Register your models here.


class IntentAdmin(admin.ModelAdmin):
    fields = ['idfa','product_id','product_price', 'advertiser_id','converted']

    list_display = ('idfa', 'product_id','product_price',  'advertiser_id','converted')

    search_fields = ['product_id','product_price',  'advertiser_id','idfa']

class ClickAdmin(admin.ModelAdmin):
    fields = ['idfa','product_id','advertiser_id','campaign_id','element_ids','converted']
    list_display = ('idfa','product_id','advertiser_id','campaign_id','element_ids','converted')
    search_fields = ['idfa','product_id','advertiser_id','campaign_id','element_ids']

class ProductAdmin(admin.ModelAdmin):
    fields = ['product_name', 'product_id', 'product_price', 'advertiser_id', 'product_image_url' ]
    list_display = ('product_name', 'product_id', 'product_name', 'product_price', 'advertiser_id', 'product_image_url')
    search_fields = ('product_name', 'product_id', 'product_name', 'product_price', 'advertiser_id', 'product_image_url')

class ElementAdmin(admin.ModelAdmin):
    fields = ['element_id', 'element_type', 'product_id', 'text', 'advertiser_id', 'campaign_id', 'impressions', 'clicks', 'conversions']
    list_display = ('element_id', 'element_type', 'product_id', 'text', 'advertiser_id', 'campaign_id', 'impressions', 'clicks', 'conversions')
    search_fields = ('element_id', 'element_type', 'product_id', 'text', 'advertiser_id', 'campaign_id', 'impressions', 'clicks', 'conversions')

class CampaignAdmin(admin.ModelAdmin):
    fields = ['active', 'campaign_id', 'advertiser_id', 'name', 'template']
    list_display = ('active', 'campaign_id', 'advertiser_id', 'name', 'template')
    search_fields = ('active', 'campaign_id', 'advertiser_id', 'name', 'template')


admin.site.register(Intent, IntentAdmin)
admin.site.register( Click, ClickAdmin)
admin.site.register( Product, ProductAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Campaign, CampaignAdmin)