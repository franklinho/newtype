from django.contrib import admin
from adserver.models import Intent
# Register your models here.


class IntentAdmin(admin.ModelAdmin):
    fields = ['idfa','product_id','advertiser_id','converted']

    list_display = ('idfa', 'product_id', 'advertiser_id','converted')

    search_fields = ['product_id', 'advertiser_id','idfa']

admin.site.register(Intent, IntentAdmin)