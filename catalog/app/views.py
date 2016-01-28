from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse
import models
# Create your views here.
def index(request):
	return render_to_response("index.html")
