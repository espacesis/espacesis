from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View

# Create your views here.
class Softday9(View):
    
    def get(self, request):
        return render(request, "pages/result.html")
        