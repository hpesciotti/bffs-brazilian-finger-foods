from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies a value by an arg."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def divide(value, arg):
    """Divides a value by an arg."""
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError):
        return 0