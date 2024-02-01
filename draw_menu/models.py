from django.db import models


class MenuModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название меню')
    slug = models.SlugField(max_length=100, verbose_name='Слаг')
    parent = models.ForeignKey(to='MenuModel', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                               verbose_name='Меню верхнего уровня')
    is_leaf = models.BooleanField(default=True, verbose_name='Является самым нижним уровнем меню')
