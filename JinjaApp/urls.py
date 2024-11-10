from django.urls import path
from JinjaApp import views

urlpatterns=[
path('',views.home,name='my_home'),
path('contact/',views.contact,name='my_contact'),
path('base/',views.base,name='my_base'),
path('about/',views.about,name='my_about')
]
