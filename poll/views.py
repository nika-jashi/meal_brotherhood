from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from poll.models import Menu, RestaurantList
from user.models import Profile


@login_required
def in_or_out(request):
    if request.method == 'POST':
        Profile.objects.update_or_create(user=request.user)
        going_out = 1 if request.POST.get('Yes') == "I'm Going Out" else 0
        Profile.objects.filter(user_id=request.user.id).update(going_out_or_not=going_out)
        return redirect('poll2')
    return render(request, 'poll/office_outside.html')


@login_required
def choose_restaurant(request):
    res = RestaurantList.objects.all()
    if request.method == 'POST':
        Profile.objects.update(user=request.user)
        res_id = RestaurantList.objects.values_list("id").filter(restaurant_name=request.POST.get("chosen")).first()[0]
        Profile.objects.filter(user_id=request.user.id).update(res_id=res_id)
        return redirect('poll3')
    context = {'restaurant': res}
    return render(request, 'poll/choosing_restaurant.html', context)


@login_required
def fill_form(request):
    return render(request, 'poll/fill_form.html')
