from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseView(LoginRequiredMixin, View):
    """View with LoginRequiredMixin and PermissionRequiredMixin."""

    pass

class BaseTemplateView(LoginRequiredMixin, TemplateView):
    """TemplateView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass

class BaseListView(
    LoginRequiredMixin,
    ListView,
):
    """ListView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass

class BaseDetailView(LoginRequiredMixin, DetailView):
    """DetailView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseCreateView(
    LoginRequiredMixin,
    CreateView,
):
    pass


class BaseUpdateView(
    LoginRequiredMixin,
    UpdateView,
):
    pass


class BaseDeleteView(
    LoginRequiredMixin,
    DeleteView,
):
    """CBV to delete a model record - both Ajax and POST requests."""

    pass