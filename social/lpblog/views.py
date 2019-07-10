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

con = pymysql.connect(host='localhost', user='root', password='Detergent#99', db='social', charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)


@api_view(('POST',))
def set_posts(request):
    cursor1 = con.cursor()
    post_id = request.POST.get('post_id')
    post_caption = request.POST.get('post_caption')
    lp = request.POST.get('lp')
    likes = request.POST.get('likes')
    post_url = request.POST.get('post_url')
    print(post_id, )
    try:
        cursor1.execute(
            ("insert into posts values({0},'{1}','{2}',{3},'{4}');").format(post_id, post_caption, lp, likes, post_url))
        cursor1.close()
    except Exception as e:
        print(e)
    return Response(status=200)


@api_view(('GET',))
def get_posts(request):
    cursor2 = con.cursor()
    cursor2.execute('select * from posts;')
    posts = cursor2.fetchall()
    cursor2.close()
    return Response(status=200, data={"posts": posts})


con.commit()
