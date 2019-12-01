from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Squirrels,Form
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.list import ListView

def all_squirrels(request):
    squirrels = Squirrels.objects.all()
    context = {
            'squirrels':squirrels
            }
    return render(request,'sightings/all.html',context)
def squirrels_details(request,Unique_squirrel_id):
    squirrel = Squirrels.objects.get(id=Unique_squirrel_id)
    return HttpResponse(f"hi,i'm {squirrel.Unique_squirrel_id}")

def update(request,squirrel_id):
    Object=get_object_or_404(Squirrels,Unique_squirrel_id=squirrel_id)
    form = Form(request.POST,instance=Object)
    context = {'form':form}
    try:
        Object=form.save(commit=False)
        Object.save()
        messages.success(request,"You've updated the data!")
        return redirect('../')
    except:
        context={
                'form':form,
                'error':"Sorry, the data can't be updated, please check again."
        }
        return render(request,'sightings/update_form.html',context)

class add(CreateView):
    model = Squirrels
    fields = '__all__'

class delete(DeleteView):
    model =Squirrels
    success_url = reverse_lazy('squirrels-list')


class ListView(ListView):
    model = Squirrels
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
# Create your views here.
