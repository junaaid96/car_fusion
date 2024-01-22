from django.views.generic import DetailView
from .models import Car
from .forms import ReviewForm
from django.contrib import messages


class CarDetailsView(DetailView):
    model = Car
    template_name = 'car_details.html'
    # context_object_name = 'car'

    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(self.request.POST)
        car = self.get_object()
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.car = car
            review.name = self.request.user
            review.email = self.request.user.email
            review.save()
            messages.success(request, 'Review submitted successfully!')
        else:
            messages.error(request, 'Invalid data! Please try again.')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        reviews = car.reviews.all()
        context["reviews"] = reviews
        context["review_form"] = ReviewForm()
        return context
