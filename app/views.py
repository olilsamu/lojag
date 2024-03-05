from django.shortcuts import render

# Create your views here.
from django.views import View
from.models import *

class IndexView(View):

    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, 'index.html', {'produtos':produtos})
    
    def post(self, request):
        pass
