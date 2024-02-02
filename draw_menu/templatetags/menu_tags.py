from django import template
from django.db.models import QuerySet

from draw_menu.models import HeadMenuModel, MenuItemModel

register = template.Library()


@register.inclusion_tag('draw_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    item_slug = context.get('params', {}).get('item_slug', None)

    menu_items = MenuItemModel.objects.filter(
        head_menu__name=menu_name).select_related('parent').select_related('head_menu')

    if item_slug:
        item = menu_items.filter(slug=item_slug).first()
        menu_temp = _create_menu_dict(menu_items, item)
    else:
        menu_temp = {}
    menu_temp['main'] = menu_items.filter(parent__isnull=True)

    return {'menu': menu_temp, 'curr': 'main'}


def _create_menu_dict(query: QuerySet, item: MenuItemModel):
    menu = {}
    while item:
        item_children = query.filter(parent=item)
        if item_children:
            menu[item] = item_children

        item = item.parent

    return menu


