from django import template
from news.models import Category
from django.db.models import *
register = template.Library()


@register.simple_tag()
def get_categories():
    return {'category': Category.objects.filter(news__is_published=True).annotate(
        count_category=Count('news')),
        'count_all': Category.objects.filter(news__is_published=True).aggregate(sum=Count('news'))}


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories, 'title': 'Новости'}
