from django.conf.urls import url
from .views import CreateAlgoView, AlgosView, AlgoDetailView

urlpatterns = [
    url(r'^create-algo/$', CreateAlgoView.as_view()),
    url(r'^algos/$', AlgosView.as_view()),
    url(r'^algos/(?P<name>[a-zA-Z]+)/$', AlgoDetailView.as_view(), name='algo-detail'),
]
