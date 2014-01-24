from django import template


register = template.Library()

@register.filter(name='date_timedelta')
def date_timedelta(date, timedelta):
    return date + timedelta