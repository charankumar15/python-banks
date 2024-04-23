from django import template


register = template.Library()

@register.filter # {{ }}
def say_hi(name):
    return "Hi "+ name

@register.filter # {{ }}
def say_message(name, message):
    return message + name

@register.simple_tag
def my_simple_tag(val1, val2 , val3, val4):
    return val1 + val2 + val3+ val4 