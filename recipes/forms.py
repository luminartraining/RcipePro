#modelform
# model

from django import forms
from django.forms import ModelForm
from recipes.models import Recipe

class CreateRecipeForm(ModelForm):
    ingradiantnts = forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Recipe
        fields=["recipe_name","ingradiantnts",
                "category",
                "recipe_img",
                "created_by"
                ]
