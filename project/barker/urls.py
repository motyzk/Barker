from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListBarksView.as_view(), name="list"),
]