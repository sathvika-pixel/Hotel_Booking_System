from django.urls import path
from . import views

urlpatterns=[

path('',views.home,name='home'),

path('hotels/',views.hotel_list,name='hotel_list'),

path('hotel/<int:id>/',views.hotel_detail,name='hotel_detail'),

]