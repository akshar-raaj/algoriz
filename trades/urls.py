from django.conf.urls import url
from .views import CreateAlgoView, AlgosView

urlpatterns = [
    url(r'^create-algo/', CreateAlgoView.as_view()),
    url(r'^algos/', AlgosView.as_view()),
]
