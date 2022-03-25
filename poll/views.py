from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from poll.models import Menu, RestaurantList, Decision
from user.models import Profile


# class InOrOut(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'poll/office_outside.html')
#
#     def post(self, request: WSGIRequest, *args, **kwargs):
#         if request.method == 'POST':
#             Profile.objects.update_or_create(user=request.user)
#
#             if request.POST.get('Yes') == "I'm Going Out":
#                 Profile.objects.filter(user_id=request.user.id).update(on_site=1)
#                 return redirect('poll:location')
#             Profile.objects.filter(user_id=request.user.id).update(on_site=0)
#             return redirect('poll:ordering')
#
#
# class ChooseRestaurant(View):
#     def get(self, request, *args, **kwargs):
#         res = RestaurantList.objects.all()
#         context = {'restaurant': res}
#         return render(request, 'poll/main.html', context)
#
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             res_id = RestaurantList.objects.values_list("id").filter(restaurant_name=request.POST.get("chosen")).first()[0]
#             Profile.objects.filter(user_id=request.user.id).update(res_id=res_id)
#             return redirect('poll:restaurant_menu')
#
#
# @login_required
# def fill_form(request):  # TODO add class based view
#     if request.method == 'POST':
#         Menu.objects.update_or_create(menu=request.POST.get('box'))
#         menu = Menu.objects.values_list("id").filter(menu=request.POST.get("box"))
#         Profile.objects.filter(user=request.user.id).update(menu=menu)
#         return redirect('poll:result')
#     return render(request, 'poll/fill_form.html')
#
#
# def results(request):
#     query_results = Profile.objects.all()
#     context = {'query_results': query_results}
#     return render(request, 'poll/results.html', context)
#
#
# def orderer(request):
#     if request.method == 'POST':
#         orders = 1 if request.POST.get('Yes') == "Yes" else 0
#         Profile.objects.filter(user_id=request.user.id).update(who_orders=orders)
#         return redirect('poll:location')
#     return render(request, 'poll/orderer.html')
#

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

        for d in decision_list:
            if d not in data:
                data[d.res.restaurant_name] = Decision.objects.filter(res=d.res)
            else:
                data[d.res.restaurant_name] += Decision.objects.filter(res=d.res)


        context = {'data': data}
        return render(request, 'poll/results.html', context)
