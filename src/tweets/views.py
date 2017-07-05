from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.
from .models import Tweet
from .forms import TweetModelForm

class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class  = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = '/tweet/create/'


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class  = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = '/tweet/create/'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy("tweet:list")

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

class TweetListlView(ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        context = super(TweetListlView, self).get_context_data(*args, **kwargs)
        return context
