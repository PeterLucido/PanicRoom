from django.shortcuts import render
from django.contrib.auth.views import LoginView

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