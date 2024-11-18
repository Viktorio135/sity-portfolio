import urllib.parse

from django import template

register = template.Library()

@register.simple_tag()
def get_name(name):
    
    name_os = urllib.parse.unquote(name)
    split_file_name = name_os.split('/')
    return split_file_name[-1]
    
    