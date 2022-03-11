import sys
import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, request,jsonify

app = Flask(__name__)
@app.route('/kenh14', methods=['GET'])
def verify():
    pages = 'https://kenh14.vn/sport.html'
    page = requests.get(pages)
    print(page.content)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='knswli need-get-value-facebook clearfix')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(str(links))
def log(message):  # simple wrapper for logging to stdout on heroku
    print(message)
    sys.stdout.flush()

