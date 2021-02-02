from datetime import datetime

from django import forms
from .models import Recipe, Image
from django.forms.models import BaseModelFormSet


class RecipeForm(forms.ModelForm):
    created = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)

    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('user',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )


class BaseImageFormSet(BaseModelFormSet):
    def clean(self):
        if any(self.errors):
            return
        for form in self.forms:
            image = form['image'].data
            if not image:
                raise (forms.ValidationError("Image is required fields"))
