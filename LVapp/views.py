from django.shortcuts import render
from .models import LVapp
# Create your views here.
def LVfunction(request):
    infoDB = LVapp.objects.all()
    return render(request,'LVapp/louisvuitton.html',{'infoDB': infoDB})

def infoProdotto(request):
    return render(request,'LVapp/infoprodotto.html')