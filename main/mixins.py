from django.views.generic import TemplateView
from .services import get_order


class OrderMixin(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = get_order()
        return context
