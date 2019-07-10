from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pymysql
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, views
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
con=pymysql.connect(host='localhost',user='root',password='Detergent#99',db='social',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)


@api_view(('POST',))
def insertintoblog(request):
    cursor1=con.cursor()
    # cursor1.execute("")
    return Response(status=200)


@api_view(('GET',))
def get_posts(request):
    cursor2=con.cursor()
    cursor2.execute('select * from posts;')
    posts=cursor2.fetchall()
    return Response(status=200,data={"posts":posts})

