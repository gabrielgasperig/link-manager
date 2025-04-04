from django import forms
from .models import Link

# Create your forms here.

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url', 'category', 'title']
