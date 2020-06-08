from django.shortcuts import render
from django.http import HttpResponse
#from app.models import Bio
#def index(request):
    #return HttpResponse("Hey Boys")

#def index(request):
    #return render(request,"index0.html",{})

#def index1(request):
    #Key = Bio.objects.all()
    #return render(request,"index1.html",{'User':Key})
def index(request):
    return render(request,"index.html",{})