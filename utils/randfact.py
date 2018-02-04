#! /usr/bin/python

import cgi
import cgitb

cgitb.enable()

import random

HTML_HEADER = 'Content-type: text/html\n\n'

Top_HTML='''
<html>
<head>
<title>Random Food Facts</title>
      <style>
      body {font-family: "Trebuchet MS", Helvetica, sans-serif;}
      div.transbox {
        margin: 30px;
        background-color: #ffffff;
        border: 1px solid black;
        opacity: 0.8;
        filter: alpha(opacity=60);
      }
      html { 
        background: url(foodBack4.jpg) no-repeat center center fixed; 
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
      }
    </style>
</head>
<body>
<div class="transbox">
<center><h1>And your random food fact is...</h1></center>
'''
Bottom_HTML='<FORM><INPUT Type="button" VALUE="Back" onClick="history.go(-1);return true;"></FORM> </div></div></body></html>'

factdict={1:'An avocado has more than twice as much potassium as a banana.',
          2:'The peanut is actually a legume, not a nut (which is why they are often roasted).',
          3:'Celery is the best vegetable source of naturally occurring sodium.',
          4:'Onions aid in cellular repair.',
          5:'Pumpkin seeds are high in zinc, which is good for the prostate and building the immune system.',
          6:'Sweet potatoes contain calcium, are high in vitamins A and C and contain thiamine',
          7:'Fruit juice can have more calories and sugar than soda.',
          8:'Adding fat to your salad can make it more healthful.',
          9:'Coconut water can be used (in emergencies) as a substitute for blood plasma.',
          10:'Carrots were originally purple!',
          11:'Honey is the only food that will never rot, it can last 3000 years.',
          12:'Scientists can turn peanut butter into diamonds!',
          13:'Fortune cookies are not a traditional Chinese custom. They were invented in early 1900 in San Francisco.',
          14:'Dynamite is made with peanuts!',
          15:"Airplane food isn't very tasty because our sense of smell and taste decrease from 50 to 20 percent.",
          16:'The jars of Nutella sold in a year could cover The Great Wall of China 8 times.',
          0:'During the average meal, you eat over 90,000 miles of DNA.',
          17: 'Almonds are a member of the peach family.',
          18:'Pumpkin flowers are edible.',
          19:'A row of corn always has an even number.',
          20:'Lettuce is a member of the sunflower family.',
          21:'Sugar is the only taste that humans are born craving.',
          22:'Egg yolks are one of the few foods that naturally contain Vitamin D.',
          23:'Some yogurt contain beef or pork gelatin.',
          24:'Chocolate was once used as currency.',
          25:'Back in the 1800s, people believed tomatoes had a powerful healing property for curing the likes of diarrhea, jaundice and indigestion.',
          26:'Honey is made from a combination of nectar and... bee vomit',
          27:'One of the most hydrating foods to eat is cucumber, made up of 96% water.',
          28:"Gelatin is made from the skin, connective tissue, and bones of animals, such as cows and pigs.",
          29:'If you put lemons and limes in water, lemons will float and limes will sink'
          }
          
def randfact():
    print HTML_HEADER
    print Top_HTML
    factno=random.randrange(30)
    print '<center><h3>'+factdict[factno]+'</h3></center>'
    print Bottom_HTML

randfact()
