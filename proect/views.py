from django.shortcuts import render
from .models import Mehmonxona, Travel, Klass

from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import TrevelineSerializer


class TravelAPIView(APIView):
    def get(self, request:Request, pk=None):
        if pk:
            try:
                tur=Travel.objects.get(pk=pk)
                return Response( TrevelineSerializer(tur).data )
            except:
                return Response({"sms":"Tur topilmadi"})
        tur = Travel.objects.all()
        return Response({'tur': TrevelineSerializer(tur, many=True).data})
    

    def post(self, request: Request):
        serializer = TrevelineSerializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)    
        tur=serializer.save()    
        return Response(TrevelineSerializer(tur).data)
    
    def put (self, request:Request, pk :int=None):
        if not pk:
            return Response({"sms":"Put iloji topilmadi"})
        try:
            tur=Travel.objects.get(pk=pk)
            serializer = TrevelineSerializer(instance=tur, data=request.data)
            serializer.is_valid(raise_exceptions=True)
            update_tur= serializer.save()
            return Response(TrevelineSerializer(update_tur).data)
        except:
            return Response({"sms":"Tur topilmadi"})
        
    def delete(self, request:Request, pk: int=None): 
        if not pk:
            return Response({"sms":"Put iloji topilmadi"})
        try:   
            tur = Travel.objects.get(pk=pk)
            tur.delete()
            return Response({"sms":"Tur topilmadi"})
        except: 
            return Response({"sms":"Tur topilmadi"})
