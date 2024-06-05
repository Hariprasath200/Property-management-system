from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('deposit',views.deposit,name='deposit'),
    path('agent',views.agent,name='agent'),
    path('bus',views.bus,name='bus'),
    path('search_results/<str:from_location>/<str:to_location>/<str:travel_date>/', views.search_results, name='search_results'),
]








































#hari
