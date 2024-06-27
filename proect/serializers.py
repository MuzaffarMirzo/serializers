from rest_framework import serializers
from .models import Travel
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class TrevelSerializer(serializers.Serializer):
   id=serializers.IntegerField(read_only=True)
   nomi=serializers.CharField(max_length=150)
   izoh=serializers.CharField()
   muddati=serializers.DateField()
   narxi=serializers.IntegerField()
   klass_id=serializers.IntegerField()
   mexmonxona_id=serializers.IntegerField()

   def create(self, validated_data):
      return Travel.objects.create(**validated_data)
   
   def update(self, instance, validated_data):
      instance.nomi=validated_data.get('nomi',instance.nomi)
      instance.izoh=validated_data.get('izoh',instance.izoh) 
      instance.muddati=validated_data.get('muddati',instance.muddati)
      instance.narxi=validated_data.get('narxi',instance.narxi)
      instance.klass=validated_data.get('klass_id',instance.klass)
      instance.mexmonxona=validated_data.get('mexmonxona_id',instance.mexmonxona)
      instance.save()
      return instance
   
    