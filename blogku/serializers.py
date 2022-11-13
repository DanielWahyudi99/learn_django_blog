from rest_framework import serializers
from .models import blogs
from .models import matematika

class blogserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = blogs
        fields = ("id" ,"title","content")

class matematikaserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = matematika
        fields = ("id" ,"x","y" ,"z")