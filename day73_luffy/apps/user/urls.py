# coding:utf8
from django.urls import path,re_path
from rest_framework.views import APIView
from rest_framework.response import Response
class Test(APIView):
    def get(self,request):
        return Response('ok,你还好吗？')


urlpatterns = [
    path('test/',Test.as_view()),
]
