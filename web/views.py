from django.shortcuts import render
from invoice.models import Invoice

# Create your views her
def index(request):
    return render(request, 'index.jinja.html')
