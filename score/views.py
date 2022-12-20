from django.shortcuts import render
from .forms import LoginForm
from django.views.generic import TemplateView

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


# Create your views here.
class LoginView(SuccessMessageMixin,FormView):
    template_name = 'index.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')
    def form_valid(self,form):
             form.save()
             return super().form_valid(form)
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index2.html'
