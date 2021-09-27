from inspect import Parameter

from django import forms

from products.models import CommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['post', 'created_at']


class ProductModelForm(forms.ModelForm):
    def ProductModel(self, request, obj, form, change):
        files = request.FILES.getlist('files')
        for f in files:
            instance = Parameter(files=f)
            instance.save()
