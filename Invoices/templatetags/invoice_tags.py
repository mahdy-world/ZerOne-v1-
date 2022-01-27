from django import template
from django.db.models import Sum

register = template.Library()
from Invoices.models import *

@register.simple_tag(name='invoice_products')
def invoice_products(inv_id):
    return InvoiceItem.objects.filter(invoice__id=inv_id)


@register.simple_tag(name='invoice_products_val')
def invoice_products_val(inv_id):
    return InvoiceItem.objects.filter(invoice__id=inv_id).aggregate(sum=Sum('total_price')).get('sum')


@register.simple_tag(name='invoice_saved')
def invoice_saved(inv_id):
    return Invoice.objects.filter(id=inv_id, saved=True)


@register.simple_tag(name='invoice_paid')
def invoice_paid(inv_id):
    return Invoice.objects.filter(id=inv_id, paid=True)


@register.simple_tag(name='invoice_out_of_warehouse')
def invoice_out_of_warehouse(inv_id):
    return Invoice.objects.filter(id=inv_id, out_of_warehouse=True)