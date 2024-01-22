from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Rating (1-10)'}))
    class Meta:
        model = Review
        fields = ['comment', 'rating']