from django.contrib.auth.models import User
from django.views.generic.list import ListView
from . import models
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.encoding import escape_uri_path
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


class LoggedInMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            pass
            url = reverse("login") + "?from=" + escape_uri_path(request.path)
            return redirect(url)
        return super().dispatch(request, *args, **kwargs)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('barker:list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user is not None and user.is_active:
            login(self.request, user)
            if self.request.GET.get('from'):
                return redirect(
                    self.request.GET['from'])  # SECURITY: check path
            return redirect('barker:list')
        form.add_error(None, "Invalid user name or password")
        return self.form_invalid(form)


class ListBarksView(ListView):
    header = "all barks"
    page_title = "Entire Barks List"
    paginate_by = 10
    model = models.Bark

    def get_queryset(self):
        return super().get_queryset().filter() #filter by followee


class UserDetailView(DetailView):
    page_title = "User Barks"
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "object"

    def header(self):
        return self.object


class CreateBarkView(LoggedInMixin, CreateView):
    header = "Bark"
    page_title = "Bark"
    model = models.Bark
    fields = (
        'content',
    )

    def get_form(self, form_class=None):
        return super().get_form(form_class)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)