from django.urls import path
from . import views
from django.conf.urls import url
from .views import all_squirrels,add
urlpatterns=[
        path('',all_squirrels),
        path('add/',views.add.as_view(),name='add'),
        ]
