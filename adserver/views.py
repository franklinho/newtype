from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from adserver.models import Intent

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the adserver index.")

def intent(request):
    idfa = request.GET.get('idfa')
    product_id = request.GET.get('product_id')
    advertiser_id = request.GET.get('advertiser_id')

    # context = {
    #     'idfa' : idfa,
    #     'product_id', product_id,
    #     'advertiser_id', advertiser_id
    # }

    if idfa is not None and product_id is not None and advertiser_id is not None:
        intents = Intent.objects.filter(idfa=idfa,product_id=product_id,advertiser_id=advertiser_id)

        if intents.count() == 0:
            i = Intent(idfa=idfa, product_id=product_id, advertiser_id = advertiser_id, converted=False)
            i.save()
            return HttpResponse("Tracking Intent. IDFA is %s. Product ID is %s. Advertiser ID is %s" % (idfa,product_id,advertiser_id))
        else:
            return HttpResponse("Intent for this combination already exists. IDFA is %s. Product ID is %s. Advertiser ID is %s" % (idfa,product_id,advertiser_id))
    else:
        return HttpResponse("Missing parameters. Are you sure you have the idfa, the product_id and the advertiser_id?")

def conversion(request):
    idfa = request.GET.get('idfa')
    product_id = request.GET.get('product_id')
    advertiser_id = request.GET.get('advertiser_id')

    if idfa is not None and product_id is not None and advertiser_id is not None:
        intents = Intent.objects.filter(idfa=idfa,product_id=product_id,advertiser_id=advertiser_id)
        print(intents)
        if intents.count() == 0:
            return HttpResponse("No associated retargeting intent. IDFA is %s. Product ID is %s. Advertiser ID is %s" % (idfa,product_id,advertiser_id))
        elif intents[0].converted == False:
            i = intents[0]
            i.converted = True
            i.save()
            return HttpResponse("Confirming conversion for this intent. IDFA is %s. Product ID is %s. Advertiser ID is %s" % (idfa,product_id,advertiser_id))
        else:
            return HttpResponse("This intent has already been confirmed. IDFA is %s. Product ID is %s. Advertiser ID is %s" % (idfa,product_id,advertiser_id))
    else:
        return HttpResponse("Missing parameters. Are you sure you have the idfa, the product_id and the advertiser_id?")