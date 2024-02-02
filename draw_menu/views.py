from django.shortcuts import render
from django.views.generic import TemplateView
from draw_menu.models import HeadMenuModel, MenuItemModel


class MainPageView(TemplateView):
    template_name = 'draw_menu/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['head_menu'] = HeadMenuModel.objects.all()
        if self.kwargs.get('menu_slug'):
            context['menu_slug'] = self.kwargs.get('menu_slug')

        if self.kwargs.get('item_slug'):
            context['item_slug'] = self.kwargs.get('item_slug')

        return context



