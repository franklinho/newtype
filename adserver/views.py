from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from adserver.models import Intent, Click, Product, Element
import random


# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the adserver index.")

def intent(request):
    idfa = request.GET.get('idfa')
    product_id = request.GET.get('product_id')
    advertiser_id = request.GET.get('advertiser_id')
    product_price = request.GET.get('product_price')

    # context = {
    #     'idfa' : idfa,
    #     'product_id', product_id,
    #     'advertiser_id', advertiser_id
    # }

    if idfa is not None and product_id is not None and advertiser_id is not None and product_price is not None:
        intents = Intent.objects.filter(idfa=idfa,product_id=product_id,advertiser_id=advertiser_id,product_price=product_price)

        if intents.count() == 0:
            i = Intent(idfa=idfa, product_id=product_id, advertiser_id = advertiser_id, converted=False, product_price=product_price)
            i.save()
            return HttpResponse("Tracking Intent. IDFA is %s. Product ID is %s. Advertiser ID is %s. Product Price is %s" % (idfa,product_id,advertiser_id, product_price))
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

def ad(request):
    request_idfa = request.GET.get('idfa')
    adcounter = 1# adcounter = random.randrange(2)
    template = None
    if adcounter == 0:
        template = loader.get_template('adserver/best_buy_ad_template.html')
        context = RequestContext(request, {})
    else:
        products = Product.objects.filter(advertiser_id='candycrush')
        product = None
        if request_idfa is not None:
            intents = Intent.objects.filter(idfa=request_idfa, converted = False).order_by('-product_price')
            if intents.count() == 0:
                product = products[random.randrange(products.count())]
            else:
                product = products.filter(product_id=intents[0].product_id)[0]
        else:
            product = products[random.randrange(products.count())]


        ctas = Element.objects.filter(advertiser_id='candycrush',element_type='cta',campaign_id = 'candycrushinterstitial')
        cta = ctas[random.randrange(ctas.count())]
        template = loader.get_template('adserver/candy_crush_ad_template.html')
        context = RequestContext(request, {
            'product_name' : product.product_name,
            'product_image_url': product.product_image_url,
            'cta': cta.text,
        })



    return HttpResponse(template.render(context))