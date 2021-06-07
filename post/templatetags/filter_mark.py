import markdown
from django.template import Library

# 实例化的对象名字必须是register
register = Library()

@register.filter
def md(value):
    return markdown.markdown(value)