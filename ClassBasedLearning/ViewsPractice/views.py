from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.views import View
# Create your function based views here.
def index(request):
    return HttpResponse('<h1>I am Function Based based View</h1>')

# Using View ClassBased View
class FirstView(View):
    def get(self, request):
        return HttpResponse('<h1>I am Class Based based View</h1>')