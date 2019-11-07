from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView
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

class PollVote(RedirectView):
    def get_redirect_url(self, **kwargs):
        opt = Option.objects.get(id=self.kwargs['oid'])
        opt.count += 1
        opt.save()
        return "/poll/{}/".format(opt.poll_id)

class PollCreate(CreateView):
    model = Poll
    fields = ['subject']
    success_url = "/poll/"

class PollUpdate(UpdateView):
    model = Poll
    fields = ['subject']
    success_url = "/poll/"