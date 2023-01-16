from django.contrib.auth import login
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from ..forms import NewDriverForm
from ..models import User, Order, DriverUser
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

@driver_required
def driver_available_orders(request):
    all_orders = Order.objects.all().filter(driver=None)
    # TODO: is_rated = False we use to get not completed orders. Need to replace with status
    usr: User=request.user
    drv = DriverUser.objects.get(user=usr)
    assigned_orders = Order.objects.filter(driver=drv).filter(is_rated=False)
    return render(request, 'main_app/driver_available_orders.html', context={'assigned_orders': assigned_orders, 'available_orders_list': all_orders})

@driver_required
def driver_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'main_app/driver_order.html', context={'order': order})

