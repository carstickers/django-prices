from django import template
from django.utils.translation import to_locale, get_language

from babel import core as babel_core
from babel import support as babel_support

from ..utils.formatting import format_price


register = template.Library()


def currencyfmt(number, currency):
    locale = babel_core.Locale.parse(to_locale(get_language()))
    support = babel_support.Format(locale)
    return support.currency(number, currency)


@register.filter
def amount(obj, format="text"):
    if format == "text":
        return format_price(obj.amount, obj.currency, html=False)
    if format == "html":
        return format_price(obj.amount, obj.currency, html=True)
    return currencyfmt(obj.amount, obj.currency)


@register.filter
def discount_amount_for(discount, price):
    return discount(price) - price
