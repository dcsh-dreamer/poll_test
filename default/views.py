from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
def poll_list(req):
    polls = Poll.objects.all()
    return render_to_response('poll_list.html', {'polls': polls})

class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['options'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return ctx
