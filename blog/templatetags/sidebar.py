from django import template
from blog.models import Category # импортируем модели
# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library() 
# регистрируем наш тег, который будет выводить шаблон right_sidebar.html
@register.inclusion_tag("blog/sidebar.html")
def show_sidebar():

    categories = Category.objects.all().order_by("name")
    return {'categories': categories}
