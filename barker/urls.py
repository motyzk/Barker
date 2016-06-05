from django.conf.urls import url

from . import views

app_name = "barker"
urlpatterns = [
    url(r'^$', views.ListBarksView.as_view(), name="list"),
    url(r'^bark/$', views.CreateBarkView.as_view(), name="bark"),
    #url(r'^(?P<pk>\d+)/$', views.UserDetailView.as_view(), name="detail_by_pk"),

    #shouldn't i do this?
    #url(r'^(?P<username>\w+)/$', views.ListBarksView.as_view(), name="detail_by_username"),

    #what do i need this for?????
    url(r'^(?P<username>\w+)/$', views.UserDetailView.as_view(), name="detail_by_username"),
]