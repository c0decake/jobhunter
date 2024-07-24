from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from Search.models import Orders, Shops
from Profile.models import User, City, District, Post, Director


@login_required
def searching(request):
    orders = Orders.objects.all()
    user = User.objects.filter(pk=request.session.get('user_id'))[0]
    return render(request,
                  'Search/searching.html',
                  {'title': 'Поиск подработки',
                   'orders': orders,
                   'user_data': user})


@login_required
def added(request):
    orders = Orders.objects.all()
    user = User.objects.filter(pk=request.session.get('user_id'))[0]
    return render(request,
                  'Search/added.html',
                  {'title': 'Добавленные',
                   'orders': orders,
                   'user_data': user})


@login_required
def adding(request):
    orders = Orders.objects.all()
    user = User.objects.filter(pk=request.session.get('user_id'))[0]
    cities = City.objects.all()
    post = Post.objects.all()
    return render(request,
                  'Search/new_job_form.html',
                  {'title': 'Новая подработка',
                   'orders': orders,
                   'user_data': user,
                   'cities': cities,
                   'post': post})


@login_required
def get_cities(request):
    try:
        cities = City.objects.all()
        districts = [{'id': city.id, 'name': city.name} for city in cities]
        return JsonResponse(districts, safe=False)
    except City.DoesNotExist:
        return JsonResponse({'error': 'City not found'}, status=404)


@login_required
def get_districts(request):
    city_id = request.GET.get('city')
    if city_id:
        try:
            districts = District.objects.filter(city__pk=city_id)
            districts = [{'id': district.id, 'name': district.name} for district in districts]
            return JsonResponse(districts, safe=False)
        except City.DoesNotExist:
            return JsonResponse({'error': 'City not found'}, status=404)
    else:
        return JsonResponse({'error': 'City ID not provided'}, status=400)


@login_required
def get_shops(request):
    district_id = request.GET.get('district')
    city_id = request.GET.get('city')
    shops = Shops.objects.all()
    if city_id:
        shops = shops.objects.filter(city_id=city_id)
    if district_id:
        shops = shops.objects.filter(district_id=district_id)
    return JsonResponse([{'id': shop.pk, 'name': shop.name} for shop in shops], safe=False)


@login_required
def get_posts(request):
    return JsonResponse([{"id": post.pk, "name": post.name} for post in Post.objects.all()], safe=False)


@login_required
def set_job(request):
    user = User.objects.filter(pk=request.session.get('user_id'))[0]
    if request.method == 'POST':
        data = request.POST
        if Director.objects.filter(user__pk=user.pk):
            Orders.objects.create(shop=Shops.objects.get(pk=data.get('shop')),
                                  district=District.objects.get(pk=data.get('district')),
                                  city=City.objects.get(pk=data.get('city')),
                                  date="2024-07-30",
                                  arrival_time=datetime.strptime(data.get('arrival_time'), '%H:%M').time(),
                                  end_time=datetime.strptime(data.get('time_end'), '%H:%M').time(),
                                  taxi_to=True if data.get('taxi_to', False) else False,
                                  taxi_from=True if data.get('taxi_from', False) else False,
                                  toilet=True if data.get('toilet', False) else False,
                                  food=True if data.get('food', False) else False,
                                  drinks=True if data.get('drinks', False) else False,
                                  min_rating=data.get('rating'),
                                  post=Post.objects.get(pk=data.get('post')),
                                  price=data.get('price'),
                                  publishing_date=datetime.now().date().strftime("%Y-%m-%d"),
                                  director=user)
        return render(request, 'Search/added.html', {'user_data': user, 'orders': Orders.objects.all()})
    else:
        return render(request, 'Search/new_job_form.html', {'user_data': user})


def additions_transform(order):
    additions = ""
    if order.toilet:
        additions += "🚽  "
    if order.taxi_to or order.taxi_from:
        additions += "🚕  "
    if order.food:
        additions += "🥐  "
    if order.drinks:
        additions += "🧃  "
    return additions


@login_required
def is_director(request):
    if Director.objects.filter(pk=request.session.get('user_id', '-1')):
        return JsonResponse({'is_director': 'True'}, safe=False)
    else:
        return JsonResponse({'is_director': 'False'}, safe=False)


@login_required
def get_orders(request):
    request_data = {x: y for x, y in request.GET.items() if y != '-1'}
    selected_city = request_data.get('city')
    selected_district = request_data.get('district')
    selected_post = request_data.get('post')
    date = request_data.get('date')
    order = request_data.get('order')
    orders = Orders.objects.all()
    if order:
        orders = orders.filter(pk=order)
    if selected_city:
        orders = orders.filter(city__pk=selected_city)
    if selected_district:
        orders = orders.filter(district__pk=selected_district)
    if selected_post:
        orders = orders.filter(post__pk=selected_post)
    if date:
        orders = orders.filter(date=date)
    if request_data.get('taxi') == 'true':
        orders = orders.filter(Q(taxi_to=True) | Q(taxi_from=True))
    if request_data.get('toilet') == 'true':
        orders = orders.filter(toilet=True)
    if request_data.get('food') == 'true':
        orders = orders.filter(food=True)
    if request_data.get('drinks') == 'true':
        orders = orders.filter(drinks=True)
    return JsonResponse([{'id': order.pk,
                          'date': order.date,
                          'work_time': f'{order.arrival_time.strftime("%H:%M")}-{order.end_time.strftime("%H:%M")}',
                          'city': order.city.name,
                          'district': order.district.name,
                          'address': order.shop.name,
                          'post': order.post.name,
                          'additions': additions_transform(order),
                          'price': order.price} for order in orders], safe=False)


def get_added_orders(request):
    orders = Orders.objects.filter(director__pk=request.session.get('user_id'))
    return JsonResponse([{'id': order.pk,
                          'date': order.date,
                          'work_time': f'{order.arrival_time.strftime("%H:%M")}-{order.end_time.strftime("%H:%M")}',
                          'city': order.city.name,
                          'district': order.district.name,
                          'address': order.shop.name,
                          'post': order.post.name,
                          'additions': additions_transform(order),
                          'price': order.price} for order in orders], safe=False)


def order_confirmation(request):
    if request.method == 'POST':
        return HttpResponse('Заказ подтвержден')
    else:
        return redirect('search:searching')
