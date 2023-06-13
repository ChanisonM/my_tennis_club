from django.urls import path
from . import views

urlpatterns = [
    path('members/' , views.members , name='members'),
    path('template/' , views.testing , name='template'),
    path('template2/' , views.template2 , name='template2')
]
