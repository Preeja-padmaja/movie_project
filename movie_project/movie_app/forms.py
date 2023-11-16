from django import forms
from.models import movie_table
class movie_form(forms.ModelForm):
    class Meta:
        model=movie_table
        fields=['name','desc','year','image']