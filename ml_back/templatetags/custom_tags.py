from django import template
register = template.Library()

@register.filter(name='info')
def info(value):
  return str(dir(value))
  

@register.filter(name='form_count')
def info_more(value):
  return len(value.forms) #works fine