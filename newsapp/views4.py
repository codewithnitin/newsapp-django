from django.shortcuts import render, HttpResponse

# Create your views here.


import requests
import json

headline = []
title = []
desc = []
url = []
content = []
r = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=newsapikey")
json_string = r.text
dict = json.loads(json_string)

for i in range(0, 5):
    var = f"{i + 1}"
    var1 = dict["articles"][i]["title"]
    var2 = dict["articles"][i]["description"]
    var3 = dict["articles"][i]["urlToImage"]
    var4 = dict["articles"][i]["content"]
    headline.append(var)
    title.append(var1)
    desc.append(var2)
    url.append(var3)
    content.append(var4)


def business(request):
    context = {
        "headline" : headline[0],
        "title" : title[0],
        "desc" : desc[0],
        "url" : url[0],
        "content" : content[0],
        "headline1": headline[1],
        "title1": title[1],
        "desc1": desc[1],
        "url1": url[1],
        "content1": content[1],
        "headline2" : headline[2],
        "title2" : title[2],
        "desc2" : desc[2],
        "url2" : url[2],
        "content2" : content[2],
        "headline3" : headline[3],
        "title3" : title[3],
        "desc3" : desc[3],
        "url3" : url[3],
        "content3" : content[3],
        "headline4" : headline[4],
        "title4" : title[4],
        "desc4" : desc[4],
        "url4" : url[4],
        "content4" : content[4],
    }
    return(render(request, "business.html", context))
    # return(HttpResponse("This is business news homepage"))
