from django.urls import path
from . import views
urlpatterns=[
    path('',views.contact),
    path('register/',views.register,name='register'),
]