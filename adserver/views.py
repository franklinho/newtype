from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from adserver.models import Intent

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the adserver index.")

def detail(request):
    idfa = request.GET.get('idfa')
    product_id = request.GET.get('product_id')
    advertiser_id = request.GET.get('advertiser_id')

    # context = {
    #     'idfa' : idfa,
    #     'product_id', product_id,
    #     'advertiser_id', advertiser_id
    # }

    intents = Intent.objects.filter(idfa=idfa,product_id=product_id,advertiser_id=advertiser_id)

    if intents.count() == 0:
        i = Intent(idfa=idfa, product_id=product_id, advertiser_id = advertiser_id, converted=False)
        i.save()
        return HttpResponse("Tracking Intent. IDFA is %s. Product ID is %s. Advertiser ID is %s" % (idfa,product_id,advertiser_id))
    else:
        return HttpResponse("Intent for this combination already exists. IDFA is %s. Product ID is %s. Advertiser ID is %s" % (idfa,product_id,advertiser_id))
