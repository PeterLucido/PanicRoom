from django.shortcuts import render

# Add the following import

# Define the home view
def home(request):
  return render(request, '<h1>Ready Panic</h1>')

def about(request):
  return render(request, 'about.html')