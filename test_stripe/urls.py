"""test_stripe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import ItemView, ItemsView, OrderView, AddToOrderView, ChangeQuantityView, DeleteFromOrderView, buy_item, success_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:id>/', ItemView.as_view(), name="item"),
    path('buy/<int:id>/', buy_item, name="buy"),
    path("item/", ItemsView.as_view(), name="items"),
    path("order/<int:id>/", OrderView.as_view(), name="order"),
    path("order/<int:orderId>/add/<int:itemId>/",
         AddToOrderView.as_view(), name="add_to_order"),
    path("order/<int:orderId>/change/<int:itemId>/",
         ChangeQuantityView.as_view(), name="change_quantity"),
    path("order/<int:orderId>/delete/<int:itemId>/",
         DeleteFromOrderView.as_view(), name="delete"),
    path("success/<int:id>/", success_view, name="success")
]
