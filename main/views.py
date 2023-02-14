from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .services import get_items, create_session, update_order, get_order, status_success
from .mixins import OrderMixin


class ItemView(OrderMixin):

    template_name = "item.html"

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        get_items(context, id)
        return context


class ItemsView(OrderMixin):

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_items(context)
        return context


class OrderView(OrderMixin):

    template_name = "order.html"

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["order"].pk != id:
            context["currentOrder"] = get_order(id)
        else:
            context["currentOrder"] = context["order"]
        return context


class AddToOrderView(View):

    def post(self, request, orderId, itemId):
        update_order(orderId, itemId)
        messages.add_message(request, messages.INFO,
                             f"Item {itemId} successfully added")
        return redirect(reverse("order", kwargs={"id": orderId}))


class ChangeQuantityView(View):

    def post(self, request, orderId, itemId):
        quantity = request.POST.get("quantity")
        update_order(orderId, itemId, quantity)
        messages.add_message(request, messages.INFO,
                             f"Quantity {itemId} successfully changed")
        return redirect(reverse("order", kwargs={"id": orderId}))


class DeleteFromOrderView(View):

    def post(self, request, orderId, itemId):
        update_order(orderId, itemId, 0)
        messages.add_message(request, messages.INFO,
                             f"Quantity for {itemId} successfully deleted")
        return redirect(reverse("order", kwargs={"id": orderId}))


def buy_item(request, id):
    session = create_session(id)
    return JsonResponse({"id": session.id})


def success_view(request, id):
    messages.add_message(request, messages.INFO,
                         f"Order {id} successfully payed")
    status_success(id)
    return redirect(reverse("order", kwargs={"id": id}))
