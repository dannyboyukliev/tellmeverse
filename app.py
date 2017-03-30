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
import datetime
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello"

@app.route('/verse')
def get_verse():  
  query = request.args.get('query')
  api_url = 'https://bible-api.com/'
  s = requests.Session()
  result = s.get(api_url + query)
  result = result.json()
  result = result.get('text')
  message = {
    "messages": [
      {"text": result},
      {"text": query}
    ]
  }
  return jsonify(message)

if __name__ == '__main__':
  app.run()
