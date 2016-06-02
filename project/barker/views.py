from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from . import models
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.encoding import escape_uri_path


# class LoggedInMixin:
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated():
#             pass
#             url = reverse("login") + "?from=" + escape_uri_path(request.path)
#             return redirect(url)
#         return super().dispatch(request, *args, **kwargs)


class ListBarksView(ListView):
    page_title = "BarkerHome"
    model = models.Bark

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


