from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Project
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'latest_project_list'
    def get_queryset(self):
		# get the last 5
	    return Project.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]
