from django import template
from django.db.models import Sum

register = template.Library()
from SpareParts.models import *

@register.simple_tag(name='order_products')
def order_products(order_id):
    return SparePartsOrderProducts.objects.filter(product_order__id=order_id)


@register.simple_tag(name='order_op3')
def order_op3(order_id):
    return SparePartsOrderOperations.objects.filter(order_number__id=order_id, operation_type=3)


@register.simple_tag(name='order_products_val')
def order_products_val(order_id):
    return SparePartsOrderProducts.objects.filter(product_order__id=order_id).aggregate(sum=Sum('product_price')).get('sum')