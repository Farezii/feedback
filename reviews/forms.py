from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=100, label='Your name', error_messages={
#         'required': 'Name field must not be empty',
#         'max_length': 'Name is too long'
#     })

#     review_text = forms.CharField(
#         label='Your feedback', max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5,)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # ['user_name', 'review_text', 'rating']
        # exclude = ['field to be hidden']
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your Feedback',
            'rating': 'Your rating',
        }
        error_messages = {
            'user_name': {
                'required': 'Name field must not be empty',
                'max_length': 'Name is too long',
            },
        }
