import re

from django import forms
from .models import News
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'photo', 'category']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'content': forms.Textarea(attrs={'class': 'form-control'}),
                   'category': forms.Select(attrs={'class': 'form-control'})}

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название новости', widget=forms.TextInput(
#         attrs={'class': 'form-control'}
#     ))
#     content = forms.CharField(label='Содержание новости', required=False, widget=forms.Textarea(
#         attrs={'class': 'form-control'}
#     ))
#     is_published = forms.BooleanField(label='Публикация', initial=True)
#     photo = forms.ImageField(label='Фото', required=False)
#     category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=Category.objects.all(),
#                                       label='Категория', widget=forms.Select(
#         attrs={'class': 'form-control'}
#     ))
