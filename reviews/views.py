from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.
# View based on classes


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name='reviews/review.html'
    success_url='/thank-you'

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/thank-you')
    #     return render(request, 'reviews/review.html', {
    #         'form': form,
    #     })
    
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
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Ayyy lmao'
        return context

# Method
# def thank_you(request):
#     return render(request, 'reviews/thank_you.html')


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data


class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context
