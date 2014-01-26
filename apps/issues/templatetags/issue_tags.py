from django import template


register = template.Library()

@register.filter(name='expected_date')
def expected_date(issue, timedelta):
    return issue.get_expected_date(timedelta)