from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from ..forms import NewPassengerForm
from ..models import User
from ..decorators import passenger_required


class PassengerSignUpView(CreateView):
    model = User
    form_class = NewPassengerForm
    template_name = 'main_app/register_passenger.html'  # to be changed after we make a separate register

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'passenger'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('passenger_page')


@passenger_required
def passenger_page(request):
    return render(request, 'main_app/passenger_page.html', {})
