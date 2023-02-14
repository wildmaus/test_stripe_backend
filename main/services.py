from .models import Item, OrderItem, Order
from django.conf import settings
from django.urls import reverse
from django.db.models import Sum
import stripe


stripe.api_key = settings.STRIPE_API_KEY


def get_items(context={}, id=None):
    if id:
        item = Item.objects.get(pk=id)
        item.price = item.price / 100
        context["item"] = item
        return context
    else:
        items = Item.objects.all()
        for item in items:
            item.price = item.price / 100
        context["items"] = items
        return context


def create_session(id):
    order = Order.objects.prefetch_related("orderItems__item").get(pk=id)
    session = stripe.checkout.Session.create(
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": orderItem.item.name,
                    "description": orderItem.item.description
                },
                "unit_amount": orderItem.item.price
            },
            "quantity": orderItem.quantity,
        } for orderItem in order.orderItems.all()],
        mode="payment",
        success_url="http://" +
        settings.ALLOWED_HOSTS[0]+":8000/" +
        reverse("success", kwargs={"id": id}),
    )
    order.status = "in_progress"
    order.save()
    return session


def get_order(id=None):
    if id:
        order = Order.objects.prefetch_related("orderItems__item").get(pk=id)
        return order
    order = Order.objects.filter(
        status="new").prefetch_related("orderItems").first()
    if not order:
        order = Order.objects.create()
        order.total_items = 0
    else:
        order.total_items = order.orderItems.aggregate(
            Sum('quantity'))["quantity__sum"]
        if not order.total_items:
            order.total_items = 0
    return order


def update_order(orderId, itemId, quantity=None):
    item = Item.objects.get(pk=itemId)
    order = Order.objects.get(pk=orderId)
    orderItem, created = OrderItem.objects.get_or_create(
        item=item, order=order)
    if not created:
        if quantity == None:
            orderItem.quantity += 1
        elif quantity == 0:
            orderItem.delete()
            return
        else:
            orderItem.quantity = quantity
        orderItem.save()


def status_success(id):
    order = Order.objects.get(pk=id)
    order.status = "success"
    order.save()
