from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Fear, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'peter-fear-collector'

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
  photos = Photo.objects.filter(fear_id=fear_id)
  return render(request, 'fears/detail.html', {'fear': fear, 'photos': photos})

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

def add_photo(request, fear_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = f"{str(uuid.uuid4())}{photo_file.name[photo_file.name.rfind('.'):]}"
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      fear_photo = Photo.objects.filter(fear_id=fear_id).first()
      if fear_photo:
          s3.delete_object(Bucket=BUCKET, Key=fear_photo.url.rsplit('/', 1)[1])
          fear_photo.delete()
      photo = Photo(url=url, fear_id=fear_id)
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3:', err)

  return redirect('fear-detail', fear_id=fear_id)