from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from adserver.models import Intent, Click, Product, Element, Campaign
import random
import stripe
from flask import Flask
from flask import request
from flask import json


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
        intents = Intent.objects.filter(idfa=idfa,product_id=product_id,advertiser_id=advertiser_id,product_price=product_price, converted=False)

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
        intents = Intent.objects.filter(idfa=idfa,product_id=product_id,advertiser_id=advertiser_id).order_by("converted")
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
    product = None
    cta = None
    template = None
    context = None
    campaigns = Campaign.objects.all()
    if request_idfa is not None:
        intents = Intent.objects.filter(idfa=request_idfa, converted = False).order_by('-product_price')
        if intents.count() > 0:
            product = Product.objects.filter(product_id=intents[0].product_id)[0]
            product_price_string = str(product.product_price)
            advertisercampaigns = campaigns.filter(advertiser_id=product.advertiser_id)
            campaign = advertisercampaigns[random.randrange(advertisercampaigns.count())]
            template_file = campaign.template
            template = loader.get_template(template_file)
            ctas = Element.objects.filter(advertiser_id=campaign.advertiser_id,element_type='cta',campaign_id = campaign.campaign_id)
            if ctas.count() > 0:
               cta = ctas[random.randrange(ctas.count())]
            context = RequestContext(request, {
                'product_name' : product.product_name,
                'product_image_url': product.product_image_url,
                'product_url' : product.product_url,
                'cta': cta.text,
            })
        else:

            adcounter = random.randrange(campaigns.count())
            campaign = campaigns[adcounter]
            template_file = campaign.template
            template = loader.get_template(template_file)
            products = Product.objects.filter(advertiser_id=campaign.advertiser_id)
            if products.count() > 0:
                product = products[random.randrange(products.count())]
            ctas = Element.objects.filter(advertiser_id=campaign.advertiser_id,element_type='cta',campaign_id = campaign.campaign_id)
            if ctas.count() > 0:
               cta = ctas[random.randrange(ctas.count())]
            context = RequestContext(request, {
                'product_name' : product.product_name,
                'product_image_url': product.product_image_url,
                'product_url' : product.product_url,
                'cta': cta.text,
            })
    else:
        campaigns = Campaign.objects.all()
        adcounter = random.randrange(campaigns.count())
        campaign = campaigns[adcounter]
        template_file = campaign.template
        template = loader.get_template(template_file)
        products = Product.objects.filter(advertiser_id=campaign.advertiser_id)
        if products.count() > 0:
            product = products[random.randrange(products.count())]
        ctas = Element.objects.filter(advertiser_id=campaign.advertiser_id,element_type='cta',campaign_id = campaign.campaign_id)
        if ctas.count() > 0:
            cta = ctas[random.randrange(ctas.count())]
        context = RequestContext(request, {
            'product_name' : product.product_name,
            'product_image_url': product.product_image_url,
            'product_url' : product.product_url,
            'cta': cta.text,
        })





    return HttpResponse(template.render(context))

def pay(request):

    stripe.api_key = "sk_test_EaktGYpD3NOrDmOXXsFNeWji"


    data = json.loads(request,raw_post_data)


    token = data['stripeToken']
    amount = data['amount']
    description = data['description']

    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency="usd",
            card=token,
            description=description
        )
    except stripe.CardError, e:
    # The card has been declined
        pass

    return HttpResponse("Success!")