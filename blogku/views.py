from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse

from .models import blogs
from .serializers import blogserializers
from rest_framework import viewsets

def index(request):
    #langkah kedua  , object title ,content dari si class di model.py
    datablog= blogs.objects.all().values()
    #perintah values , data dictionay  , datablog itu list, all values itu dictionary
    #all ambil di database sqlite
    template = loader.get_template('blogygdisubmit.html')
    context = {
        "datakeyku" : datablog
    }
    #return HttpResponse("Hellloo World")
    return HttpResponse(template.render(context,request))
def firstpage(request):
    template = loader.get_template('index.html')

    return HttpResponse(template.render({},request))

def addblogviewsku(request):
    titleku = request.POST["titlevariableku"]
    contentku = request.POST["contentvariableku"]
    blogku = blogs(title =titleku ,content = contentku) #blogs adalah kelas di model.py , blogku adalah object
    blogku.save() # ini masuk ke database
    return HttpResponseRedirect(reverse("indexku")) # ambil alias

#form untuk melakukan update
def updatepageviewsku(request,idnya):
    datablog = blogs.objects.get(id =idnya)
    template = loader.get_template('updateku.html')

    contextupdatenya = {
        "datakeyupdateku": datablog
    }
    return HttpResponse(template.render(contextupdatenya, request))


def updatepageactionviewsku(request,idnya):
    datablog = blogs.objects.get(id=idnya)
    titleku = request.POST["titlevariableku"]
    contentku = request.POST["contentvariableku"]

    datablog.title = titleku
    datablog.content = contentku
    datablog.save()

    return HttpResponseRedirect(reverse("indexku"))  # ambil alias


def deleteactionviewsku (request,idnya):
    datablog = blogs.objects.get(id=idnya)
    datablog.delete()

    return HttpResponseRedirect(reverse("indexku"))  # ambil alias

class blogviewset(viewsets.ModelViewSet):
    queryset = blogs.objects.all()
    serializer_class = blogserializers
