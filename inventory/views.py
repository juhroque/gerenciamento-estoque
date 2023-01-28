from django.shortcuts import render
from inventory.models import Inventory

def index(request):
    produtos = Inventory.objects.all()
    return render(request, 'inventory/index.html', {'rows': produtos})