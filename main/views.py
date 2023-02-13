from django.views.generic import View, ListView
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import stripe
import json
from .services import get_item
from .models import Item


stripe.api_key = settings.STRIPE_API_KEY


class ItemView(View):
    def get(self, request, id):
        return render(request=request, template_name="item.html", context=get_item(id))

    def post(self, request, id):
        pass


def buy_item(request, id):
    item = Item.objects.get(pk=id)
    session = stripe.checkout.Session.create(
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": item.name,
                    "description": item.description
                },
                "unit_amount": item.price
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://" +
        settings.ALLOWED_HOSTS[0]+f":8000/success/{item.pk}/",
    )
    return JsonResponse({"id": session.id})


def success_view(request, id):
    return HttpResponse(f"You successfully bought Item {id}")
