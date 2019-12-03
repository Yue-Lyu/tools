from django.urls import path
from . import views
from django.conf.urls import url
from .views import all_squirrels,add
urlpatterns=[
        path('sightings/',all_squirrels),
        path('sightings/add/',views.add.as_view(),name='add'),
        path('map/',views.showmap,name='showmap'),
        path('sightings/<squirrel_id>/', views.update,name='update'),
        path('sightings/<squirrel_id>/delete/',views.delete,name='delete'),
        ]
