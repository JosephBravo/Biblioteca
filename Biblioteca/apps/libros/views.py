from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'index.html')


def homepage(request):
	return render_to_response('homepage.html',
			context_instance=RequestContext(request))