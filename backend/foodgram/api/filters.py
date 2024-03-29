import django_filters
from django_filters.widgets import BooleanWidget
from rest_framework.filters import SearchFilter

from recipes.models import Recipe


class CustomFilter(django_filters.FilterSet):
    author = django_filters.AllValuesMultipleFilter(field_name='author__id')
    tags = django_filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = django_filters.BooleanFilter(
        field_name='is_favorited',
        widget=BooleanWidget()
    )
    is_in_shopping_cart = django_filters.BooleanFilter(
        field_name='is_in_shopping_cart',
        widget=BooleanWidget()
    )

    class Meta:
        model = Recipe
        fields = ['author', 'tags', 'is_favorited', 'is_in_shopping_cart']


class CustomSearchFilter(SearchFilter):
    search_param = 'name'
