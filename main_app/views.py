from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 

from .models import Fear

# Define the home view

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('fear-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def fear_index(request):
  fears = Fear.objects.filter(user=request.user)
  return render(request, 'fears/index.html', {'fears': fears})

@login_required
def fear_detail(request, fear_id):
  fear = Fear.objects.get(id=fear_id)
  return render(request, 'fears/detail.html', {'fear': fear})

class FearCreate(LoginRequiredMixin, CreateView):
  model = Fear
  fields = ['name', 'description', 'conquered']
  success_url = '/fears/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FearUpdate(LoginRequiredMixin, UpdateView):
  model = Fear
  fields = ['name', 'description', 'conquered']

class FearDelete(LoginRequiredMixin, DeleteView):
  model = Fear
  success_url = '/fears/'
