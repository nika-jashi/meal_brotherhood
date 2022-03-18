from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from poll.forms import BaseForm
from poll.models import Questionary, RestaurantsList


@login_required
def in_or_out(request):
    if request.method == 'POST':
        Questionary.objects.update_or_create(user=request.user)
        going_out = 1 if request.POST.get('Yes') == "I'm Going Out" else 0
        Questionary.objects.filter(user_id=request.user.id).update(going_out=going_out)
        return redirect('poll2')
    return render(request, 'poll/office_outside.html')


@login_required
def choose_restaurant(request):
    res = RestaurantsList.objects.all()
    if request.method == 'POST':
        Questionary.objects.update(user=request.user)
        for r in res:
            if request.POST.get('chosen') == str(r):
                Questionary.objects.filter(user_id=request.user.id).update(restaurants=r)
                return redirect('poll3')
    context = {'restaurant': res}
    return render(request, 'poll/choosing_restaurant.html', context)


@login_required
def fill_form(request):
    return render(request, 'poll/fill_form.html')
