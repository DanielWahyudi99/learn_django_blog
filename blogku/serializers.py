from rest_framework import serializers
from .models import blogs

class blogserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = blogs
        fields = ("id" ,"title","content")

