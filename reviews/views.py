from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

# Create your views here.
#View based on classes
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, 'reviews/review.html', {
            'form': form,
        })
        
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, 'reviews/review.html', {
            'form': form,
        })
# View based on methods
# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             # Saving a form to a model
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating'],)
#             # review.save()
            
#             # Saving a ModelForm
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/review.html', {
#         'form': form,
#     })

# Class
class ThankYouView(TemplateView):
    template_name='reviews/thank_you.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Ayyy lmao'
        return context
 
# Method
# def thank_you(request):
#     return render(request, 'reviews/thank_you.html')

class ReviewsListView(TemplateView):
    template_name='reviews/review_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context