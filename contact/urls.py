from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('messages/', views.messages_list, name='messages_list'),
]
