from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Add the following import

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def fear_index(request):
  return render(request, 'fears/index.html', { 'fears': fears })

class Fear:

  def __init__(self, name, description, id):
    self.name = name
    self.description = description
    self.conquered = False


fears = [
  Fear('Spiders', '8 legs, 8 eyes, 8 reasons to be afraid', True),
  Fear('Heights', 'Don\'t look down', False),
  Fear('Clowns', 'They\'re not funny', False),
  Fear('Needles', 'They\'re sharp', False),
  Fear('Flying', 'It\'s not natural', False),
  Fear('Public Speaking', 'Just imagine everyone in their underwear', False),
]

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('fear-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})