from django.urls import path
from . import views
from django.conf.urls import url
from .views import all_squirrels,add
urlpatterns=[
        path('sightings/',views.all_squirrels),
        path('sightings/add/',views.add,name='add'),
        path('map/',views.showmap,name='showmap'),
        path('sightings/stats/',views.stats,name='stats'),
        path('sightings/<squirrel_id>/', views.update,name='update'),
        path('sightings/<squirrel_id>/delete/',views.delete,name='delete'),
        ]
