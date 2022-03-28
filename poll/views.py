from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from poll.models import Menu, RestaurantList, Decision
from user.models import Profile


class Main(View):
    def get(self, request, *args, **kwargs):
        res = RestaurantList.objects.all()
        context = {'restaurant': res}
        return render(request, 'poll/main.html', context)

    def post(self, request: WSGIRequest, *args, **kwargs):
        Decision.objects.update_or_create(user_id=request.user.id)
        if request.POST.get('Yes') == "outside":
            Decision.objects.filter(user_id=request.user.id).update(on_site=True)
        else:
            Decision.objects.filter(user_id=request.user.id).update(on_site=False)
        if request.POST.get('chosen'):
            res_id = RestaurantList.objects.values_list("id").filter(
                restaurant_name=request.POST.get("chosen")).first()[0]
            Decision.objects.filter(user_id=request.user.id).update(res_id=res_id)
        if request.POST.get('text'):
            Menu.objects.update_or_create(menu=request.POST.get('text'))
            menu = Menu.objects.values_list("id").filter(menu=request.POST.get("text"))
            Decision.objects.filter(user=request.user.id).update(menu=menu)
        if request.POST.get('will_pay'):
            Decision.objects.filter(user_id=request.user.id).update(orderer=True)
        else:
            Decision.objects.filter(user_id=request.user.id).update(orderer=False)
        return redirect('poll:result')


class Result(View):
    def get(self, request, *args, **kwargs):
        decision_list = Decision.objects.all()
        data = {}

        for d_object in decision_list:
            if d_object not in data:
                data[d_object.res.restaurant_name] = Decision.objects.filter(res=d_object.res)
            else:
                data[d_object.res.restaurant_name] += Decision.objects.filter(res=d_object.res)

        context = {'data': data}
        return render(request, 'poll/results.html', context)
