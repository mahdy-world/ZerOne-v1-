from django import template
register = template.Library()
from SpareParts.models import *

@register.simple_tag(name='order_products')
def order_products(order_id):
    return SparePartsOrderProducts.objects.filter(product_order__id=order_id)