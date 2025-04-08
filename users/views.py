from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from users.models import User
from users.forms import UserCreateForm
from django.contrib import messages
from django.shortcuts import HttpResponse

# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/register.html"
    success_url = reverse_lazy("account_login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # hash the password
        user.save()
        messages.success(self.request, "User Created Successfully.")
        return HttpResponse(reverse("account_login"))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))