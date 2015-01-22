from django.contrib import admin
from adserver.models import Intent,Click
# Register your models here.


class IntentAdmin(admin.ModelAdmin):
    fields = ['idfa','product_id','advertiser_id','converted']

    list_display = ('idfa', 'product_id', 'advertiser_id','converted')

    search_fields = ['product_id', 'advertiser_id','idfa']

class ClickAdmin(admin.ModelAdmin):
    fields = ['idfa','product_id','advertiser_id','campaign_id','element_ids','converted']
    list_display = ('idfa','product_id','advertiser_id','campaign_id','element_ids','converted')
    search_fields = ['idfa','product_id','advertiser_id','campaign_id','element_ids']

admin.site.register(Intent, IntentAdmin)
admin.site.register( Click, ClickAdmin)