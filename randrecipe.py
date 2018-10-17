#! /usr/bin/python

import cgi
import cgitb

cgitb.enable()

import urllib2
import urllib
import json
import random

HTML_HEADER = 'Content-type: text/html\n\n'

Top_HTML='''
<html>
<head>
<title>Random Recipe Generator</title>
      <style>
      body {font-family: "Trebuchet MS", Helvetica, sans-serif;}
      div.transbox {
        margin: 30px;
        background-color: #ffffff;
        border: 1px solid black;
        opacity: 0.8;
        filter: alpha(opacity=60);
      }
    </style>
</head>
<body background="foodBack5.jpg">
<div class="transbox">
<center><h1>And your random recipe is...</h1></center>
<center><p>(NOTE: click the link to get better and more detailed recipes)</p></center>
'''
Bottom_HTML='<FORM><INPUT Type="button" VALUE="Back" onClick="history.go(-1);return true;"></FORM> </div></div></body></html>'

numbtofooddict={
    0:"chicken",
    1:"ice%20cream",
    2:"pie",
    3:"donut",
    4:"bread",
    5:"cheese",
    6:"milk",
    7:"eggs",
    8:"orange",
    9:"steak",
    10:"lamb",
    11:"sausage",
    12:"peanuts",
    13:"shrimp",
    14:"clam",
    15:"soup",
    16:"chocolate",
    17:"cake",
    18:"cupcake",
    19:"cookie"
    }

def main():
    print HTML_HEADER
    print Top_HTML
    recipeno=random.randrange(20)
    recipe=numbtofooddict[recipeno]
    request = urllib2.Request('http://food2fork.com/api/search?key=de39c04491ac7b525f9a7de0a2e366a0&q='+recipe)
    handle=urllib2.urlopen(request)
    content=json.load(handle)
    if content.has_key('error'):
        if content["error"]=="limit":
            print "<center> The maximum amount of random recipe retrievals have been conducted today. Please come back tomorrow!! </center>"
            return
    print '<center><a href='+content["recipes"][0]["f2f_url"]+'>'+content["recipes"][0]['title']+'</a></center>'+'<br>'
    image=content["recipes"][0]["image_url"]
    print '<center><img src='+image+' height=200 width=300></center>'+'<br><br>'
    idd= content["recipes"][0]["recipe_id"]
    newreq=urllib2.Request('http://food2fork.com/api/get?key=de39c04491ac7b525f9a7de0a2e366a0&q&rId='+idd)
    newhandle=urllib2.urlopen(newreq)
    newcontent=json.load(newhandle)
    for i in newcontent["recipe"]["ingredients"]:
        print str(i)+'<br>'
    print Bottom_HTML

main()























