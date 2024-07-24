from django.urls import path
from .views import *

app_name = 'search'

urlpatterns = [
    path('', searching, name='searching'),
    path('added/', added, name='added_jobs'),
    path('adding/', adding, name='adding_job'),
    path('get_cities/', get_cities, name='get_cities'),
    path('get_districts/', get_districts, name='get_districts'),
    path('get_shops/', get_shops, name='get_shops'),
    path('get_posts/', get_posts, name='get_posts'),
    path('get_orders/', get_orders, name='get_orders'),
    path('get_added_orders/', get_added_orders, name='get_added_orders'),
    path('order_confirmation', order_confirmation, name='order_confirmation'),
    path('set_job/', set_job, name='set_job'),
    path('is_director/', is_director, name='director_check')
]
