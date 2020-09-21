from mptt.forms import TreeNodeChoiceField
from hierarchyapp.models import File
from django import forms

class NewItemForm(forms.Form):
    name = forms.CharField(max_length=200)
    parent = TreeNodeChoiceField(queryset=File.objects.all())