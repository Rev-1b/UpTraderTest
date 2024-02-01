from django import template
from draw_menu.models import MenuModel

register = template.Library()


@register.inclusion_tag('draw_menu/menu.html')
def draw_menu(main_menu):
    main_menu = MenuModel.objects.filter(name=main_menu)
    return {
        'main_menu': main_menu
    }