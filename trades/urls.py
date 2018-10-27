from django.conf.urls import url
from .views import CreateAlgoView

urlpatterns = [
    url(r'^create-algo/', CreateAlgoView.as_view()),
]
