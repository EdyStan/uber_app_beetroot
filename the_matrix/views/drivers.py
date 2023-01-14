from django.contrib.auth import login
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from ..forms import NewDriverForm
from ..models import User
from ..decorators import driver_required


class DriverSignUpView(CreateView):
    model = User
    form_class = NewDriverForm
    template_name = 'main_app/register_driver.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'driver'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('driver_page')


@driver_required
def driver_page(request):
    return render(request, 'main_app/driver_page.html', {})
