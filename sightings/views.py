from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrels

def all_squirrels(request):
    squirrels = Squirrels.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)
def squirrels_details(request,Unique_squirrel_id):
    squirrel = Squirrels.objects.get(id=Unique_squirrel_id)
    return HttpResponse(f"hi,i'm {squirrel.Unique_squirrel_id}")

# Create your views here.
