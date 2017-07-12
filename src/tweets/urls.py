from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
    TweetDetailView, 
    TweetListlView, 
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView
    )


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListlView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
