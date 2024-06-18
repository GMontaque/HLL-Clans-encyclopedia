from django import template

register = template.Library()

@register.filter
def secure_url(url):
    if url.startswith('http://'):
        return url.replace('http://', 'https://')
    return url
