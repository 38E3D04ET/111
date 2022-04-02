from django_filters import FilterSet, DateFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'category__name': ['icontains'],
            'source__name': ['icontains'],
            'date__name': ['icontains'],

        }

class X(FilterSet):
    date = DateFromToRangeFilter()
    class Meta:
        model = Post
        fields = ['date']