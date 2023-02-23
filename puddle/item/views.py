from django.shortcuts import render, get_object_or_404

from .models import Item


# Create your views here.
def detail(request, primary_key):
    item = get_object_or_404(Item, pk=primary_key)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=primary_key)
    return render(request, "item/detail.html", {"item": item, "related_items": related_items})
