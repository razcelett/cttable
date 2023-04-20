from django import template

register = template.Library()

@register.filter
def contains_numbers(value):
    return any(char.isdigit() for char in value)