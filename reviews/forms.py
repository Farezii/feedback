from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100, label='Your name', error_messages={
        'required': 'Name field must not be empty',
        'max_length': 'Name is too long'
    })

    review_text = forms.CharField(
        label='Your feedback', max_length=200, widget=forms.Textarea)
    rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5)
