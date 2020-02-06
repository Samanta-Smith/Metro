from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class ArticleView(APIView):
    def get(self, request):

        return Response("Сделайте Post запрос для проверки")
    def post(self, request):

       metro = request.data
       result ={
	      "unchanged": [],
	      "updated": [],
	      "deleted": []
       }
       list = []
       r = requests.get('https://api.hh.ru/metro/1')
       r = r.json()
       r = r.get("lines")
       for i in r:
           p = i.get("stations")
           for x in p:
               t = x.get("name")
               list.append(t)

       for name in metro:
           if name in list:
               result['unchanged'].append(name)
           else:
               result['updated'].append(name)
       for name in list:
           if not name in result['updated']:
               result['deleted'].append(name)

       return Response(result)
