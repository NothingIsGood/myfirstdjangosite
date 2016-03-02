from django import template
from blog.models import Page
register = template.Library() 

@register.inclusion_tag("blog/menu.html")
def show_menu():
    pages = Page.objects.all()
    return {'pages': pages}