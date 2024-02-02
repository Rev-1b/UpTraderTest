from django import template
from django.db.models import QuerySet

from draw_menu.models import HeadMenuModel, MenuItemModel

register = template.Library()


@register.inclusion_tag('draw_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItemModel.objects.filter(head_menu__name=menu_name).select_related('parent')


def _create_menu_dict(query: QuerySet, item_slug: str):
    item: MenuItemModel = query.filter(slug=item_slug)
    if not item.parent:
        head_items = query.filter(parent__isnull=True)






