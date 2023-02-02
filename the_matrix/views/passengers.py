from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect

from ..forms import NewPassengerForm, NewOrderForm, AddMoneyForm
from ..models import User, PassengerUser, Order, OrderStatus
from ..decorators import passenger_required
from chat.models import Room


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


# @passenger_required
# def passenger_new_order(request):
#     usr: User=request.user
#     passenger = PassengerUser.objects.get(user=usr)
#     available_orders = Order.objects.filter(passenger=passenger).filter(~Q(status=OrderStatus.COMPLETED)) # ~ == NOT. Here we return only active orders for passenger
#     context = {
#         'order': available_orders.last,
#         'google_api_key':settings.GOOGLE_API_KEY
#         }
#     return render(request, 'main_app/passenger_new_order.html', context=context)


@passenger_required
def passenger_new_order(request):
    print(request.POST)
    usr: User = request.user
    passenger = PassengerUser.objects.get(user=usr)
    available_orders = Order.objects.filter(passenger=passenger).filter(
        ~Q(status=OrderStatus.COMPLETED))  # ~ == NOT. Here we return only active orders for passenger
    last_order = available_orders.last()
    if last_order is None:
        last_order = Order(passenger=passenger, status=OrderStatus.NEW_ORDER, price=6.0)
        last_order.save()
    if last_order.status == OrderStatus.NEW_ORDER:
        data = {
            'start_location': f"({last_order.start_location_lat}, {last_order.start_location_lon})",
            'end_location': f"({last_order.destination_lat}, {last_order.destination_lon})",
            'price': last_order.price}
        form = NewOrderForm(initial=data)
        context = {
            'order': last_order,
            'order_status_label': OrderStatus(last_order.status).label,
            'form': form,
            'google_api_key': settings.GOOGLE_API_KEY
        }
        return render(request, 'main_app/passenger_new_order.html', context=context)
    else:
        return HttpResponseRedirect('/passenger_start_order/')


@passenger_required
def passenger_start_order(request):
    usr: User = request.user
    passenger = PassengerUser.objects.get(user=usr)
    available_orders = Order.objects.filter(passenger=passenger).filter(
        ~Q(status=OrderStatus.COMPLETED))  # ~ == NOT. Here we return only active orders for passenger
    last_order = available_orders.last()
    if not last_order:
        return HttpResponseRedirect('/passenger_new_order/')
    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        print(f"---------!!!!! {form.data}")
        if form.is_valid():  # TODO: Need to validate form data
            print(f"BOOOOOOM!!!!! {form.data}")
            start_coords = form.startCoordinates()
            end_coords = form.stopCoordinates()
            last_order.price = form.price_value()
            last_order.destination_lat = end_coords[0]
            last_order.destination_lon = end_coords[1]
            last_order.start_location_lat = start_coords[0]
            last_order.start_location_lon = start_coords[1]
            last_order.status = OrderStatus.UNASSIGNED
            last_order.save()
        elif 'button' in request.POST:
            action = request.POST['button']
            if last_order.driver is not None:
                current_order_room = Room.objects.get(slug=f"{last_order.driver.user.username}_chat_order")
                current_order_room.user1 = None
                current_order_room.save()
            if action == 'CANCEL':
                if last_order.status == OrderStatus.UNASSIGNED and last_order.passenger == passenger:
                    last_order.status = OrderStatus.NEW_ORDER
                    last_order.driver = None
                    last_order.save()
                if last_order.status == OrderStatus.ASSIGNED and last_order.passenger == passenger:
                    last_order.status = OrderStatus.NEW_ORDER
                    need_to_pay = last_order.price * 0.5
                    last_order.driver.amount_of_money += need_to_pay
                    last_order.passenger.amount_of_money -= need_to_pay
                    last_order.driver = None
                    last_order.passenger.save()
                    last_order.save()
                if last_order.status == OrderStatus.IN_PROGRESS and last_order.passenger == passenger:
                    last_order.status = OrderStatus.COMPLETED
                    need_to_pay = last_order.price * 0.8
                    last_order.driver.amount_of_money += need_to_pay
                    last_order.passenger.amount_of_money -= need_to_pay
                    last_order.driver.save()
                    last_order.passenger.save()
                    last_order.save()
            elif action == 'COMPLETE':
                if last_order.status == OrderStatus.IN_PROGRESS and last_order.passenger == passenger:
                    last_order.status = OrderStatus.COMPLETED
                    need_to_pay = last_order.price
                    last_order.driver.amount_of_money += need_to_pay
                    last_order.passenger.amount_of_money -= need_to_pay
                    last_order.driver.save()
                    last_order.passenger.save()
                    last_order.save()
                    # TODO: Add redirect on screen to set driver's rate
        else:
            print(f"ERROR!!!\n{form.errors.as_text}")
    if last_order.status == OrderStatus.NEW_ORDER:
        return HttpResponseRedirect('/passenger_new_order/')

    context = {
        'order': last_order,
        'order_status_label': OrderStatus(last_order.status).label,
        'google_api_key': settings.GOOGLE_API_KEY
    }
    return render(request, 'main_app/passenger_new_order.html', context=context)


@passenger_required
def passenger_income(request):
    usr: User = request.user
    passenger = PassengerUser.objects.get(user=usr)
    income = passenger.amount_of_money
    return render(request, 'main_app/passenger_income.html', context={'income': income})


@passenger_required
def passenger_add_money(request):
    usr: User = request.user
    passenger = PassengerUser.objects.get(user=usr)
    income = passenger.amount_of_money
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            passenger.amount_of_money += form.cleaned_data['amount']
            passenger.save()
            messages.success(request, 'Data was successfully submitted!')
    else:
        form = AddMoneyForm()
        messages.error(request, 'There was a problem while submitting your data! Try again!')
    return render(request, 'main_app/passenger_add_money.html', {'form': form, 'income': income, 'passenger': passenger})


@passenger_required
def passenger_executed_orders(request):
    usr: User = request.user
    passenger = PassengerUser.objects.get(user=usr)
    executed_orders = Order.objects.filter(passenger=passenger).filter(status=OrderStatus.COMPLETED)
    return render(request, 'main_app/passenger_old_orders.html', context={'executed_orders': executed_orders})
