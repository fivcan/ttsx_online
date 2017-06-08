# coding=utf-8
from django.template import Library

register = Library()


@register.filter
def cheng(num1, num2):
    return num1*num2