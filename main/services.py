from .models import Item


def get_item(id):
    item = Item.objects.get(pk=id)
    item.price = item.price / 100
    return {"item": item}
