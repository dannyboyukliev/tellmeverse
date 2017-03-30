# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import re
import time
from bs4 import BeautifulSoup
from flask import Flask, request, render_template, jsonify
import random
import urllib
from firebase import Firebase
import datetime

app = Flask(__name__)

@app.route('/verse')
def get_verse():
    query = request.args.get('query')
    # api_url = 'https://bible-api.com/'
    # head = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
    # s = requests.Session()
    # result = s.get(api_url + query, headers=head)
    # result = result.json()
    # result = result.get('result')
    # fulfil = result.get('fulfillment')
    # data= fulfil.get('data')
    # if data is None:
    #     speech= fulfil.get('speech')
    #     fb={"text": speech}
    # else:    
    #     fb = data.get('facebook')
    # element=[]
    # element.append(fb)
    # res = json.dumps(element, indent=4)
    # r = make_response(res)
    # #r.headers['Content-Type'] = 'application/json'
    # return r
    message = {
        "messages": [
            {"text": "danny"}
        ]
    }
    element=[]
    element.append(message)
    res = json.dumps(element, indent=0)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
