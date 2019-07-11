from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pymysql
import random
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, views
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(('POST',))
def set_posts(request):
    print("Calling set post")
    import uuid
    import random
    con = pymysql.connect(host='localhost', user='root', password='Detergent#99', db='social', charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor1 = con.cursor()
    post_caption = request.POST.get('caption')
    post_id = random.randint(1,100)
    lp = request.POST.get("caption")
    likes = 43
    post_url = request.POST.get('pic')
    print(post_id, post_caption, lp, likes, post_url)
    try:
        cursor1.execute(
            ("insert into posts values({0},'{1}','{2}',{3},'{4}');").format(post_id, post_caption, lp, likes, post_url))
        cursor1.close()
        con.commit()
        con.close()
    except Exception as e:
        print(e)
    return HttpResponse("200")


@api_view(('GET',))
def get_posts(request):
    con = pymysql.connect(host='localhost', user='root', password='Detergent#99', db='social', charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor2 = con.cursor()
    cursor2.execute('select * from posts')
    posts = cursor2.fetchall()
    cursor2.close()
    con.commit()
    con.close()
    return Response(status=200, data={"posts": posts})



