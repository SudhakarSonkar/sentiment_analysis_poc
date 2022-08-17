import json
from typing import OrderedDict
import requests
from re import T
from flask import Flask
from flask import request
from textblob import TextBlob
app= Flask(__name__)

def review(data):
    feedback=data
    blob=TextBlob(feedback)
    list=[]
    list.append(blob.sentiment)
    return list


def formatoutput(score):
    if score[0][0] > 0:
        output = OrderedDict({
            "total_review":1,
            "positive_review":1,
            "negative_review":0,
            "neutral_review":0,
            "result":"positive"
            })
    elif score[0][0] < 0:
        output=OrderedDict({
            "total_review":1,
            "positive_review":0,
            "negative_review":1,
            "neutral_review":0,
            "result":"negative"
        })
    else:
        output=OrderedDict({
            "total_review":1,
            "positive_review":0,
            "negative_review":0,
            "neutral_review":1,
            "result":"neutral"
        })

    return output



@app.route('/sentiment',methods=['POST'])
def get():
    data = request.get_json()
    score=review(data)
    result=formatoutput(score)
    return OrderedDict(result)

if __name__ == "__main__":
    app.run(debug = True)    