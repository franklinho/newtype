from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from adserver.models import Intent, Click


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

def click(request):
    idfa = request.GET.get('idfa')
    product_id = request.GET.get('product_id')
    advertiser_id = request.GET.get('advertiser_id')
    element_ids = request.GET.get('element_ids')
    campaign_id = request.GET.get('campaign_id')
    r = request.GET.get('r')

    if idfa is not None and product_id is not None and advertiser_id is not None and element_ids is not None and campaign_id is not None:
        clicks = Click.objects.filter(idfa=idfa, product_id=product_id,advertiser_id = advertiser_id, element_ids=element_ids, campaign_id=campaign_id)
        if clicks.count() == 0:
            c = Click(idfa=idfa, product_id=product_id, advertiser_id = advertiser_id, campaign_id = campaign_id, converted=False, element_ids = element_ids)
            c.save()
            if r is not None:
                res = HttpResponse(r, status=302)
                res['Location'] = r
                return res
            else:
                return HttpResponse("Tracking Click. IDFA is %s. Product ID is %s. Advertiser ID is %s. Campaign ID is %s. Element IDs are %s" % (idfa,product_id,advertiser_id,campaign_id, element_ids))
        else:
            if r is not None:
                res = HttpResponse(r, status=302)
                res['Location'] = r
                return res
            else:
                return HttpResponse("Click for this combination already exists. IDFA is %s. Product ID is %s. Advertiser ID is %s" % (idfa,product_id,advertiser_id))
    elif r is not None:
        return HttpResponseRedirect(r)
    else:
        return HttpResponse("There is no redirect 'r' parameter")