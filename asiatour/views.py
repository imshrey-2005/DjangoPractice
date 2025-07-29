from django.shortcuts import render
from django.http import HttpResponse
from asiatour.models import Tour  #
# Create your views here.
def index(request):
   tours = Tour.objects.all()  # Fetch all tours from the database
   context = {'tours': tours}  # Prepare context with tours
   return render(request, 'tours/index.html', context)