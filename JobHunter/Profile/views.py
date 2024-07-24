from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Profile.models import User


@login_required
def profile(request):
    user = User.objects.filter(pk=request.session.get('user_id'))[0]
    data = {
        'block_status': user.status,
        'photo': user.photo,
        'name': f"{user.last_name} {user.first_name} {user.father_name}",
        'post': user.post,
        'register_date': user.date_joined,
        'sub': user.subs,
        'birthday': user.birth_day,
        'email': user.email,
        'phone': user.phone,
        'tg': user.telegram_id
    }
    return render(request, 'Profile/profile.html', {'user_data': data})
