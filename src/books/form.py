from django.forms import ModelForm, ImageField, Textarea, CharField

from .models import Review

class ReviewForm(ModelForm):
    image = ImageField(
        required=False, 
    )
    review = CharField(widget=Textarea(attrs={'placeholder':"Write your review here"})
   
    )
    class Meta:
        model = Review
        fields = ('review', 'image')