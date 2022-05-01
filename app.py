import sys
import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, request,jsonify

app = Flask(__name__)
@app.route('/Kenh14Sport', methods=['GET'])
def Kenh14Sport():
    pages = 'https://kenh14.vn/sport.chn'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='knswli need-get-value-facebook clearfix')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)
@app.route('/kenh14TheGioi', methods=['GET'])
def kenh14TheGioi():
    pages = 'https://kenh14.vn/the-gioi.chn'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='knswli need-get-value-facebook clearfix')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)
@app.route('/kenh14HocDuong', methods=['GET'])
def kenh14HocDuong():
    pages = 'https://kenh14.vn/hoc-duong.chn'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='knswli need-get-value-facebook clearfix')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)
@app.route('/kenh14DoiSong', methods=['GET'])
def kenh14DoiSong():
    pages = 'https://kenh14.vn/doi-song.chn'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='knswli need-get-value-facebook clearfix')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)

@app.route('/kenh14Musik', methods=['GET'])
def kenh14Musik():
    pages = 'https://kenh14.vn/musik.chn'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='knswli need-get-value-facebook clearfix')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)

@app.route('/vnexpressTheGioi', methods=['GET'])
def vnexpressTheGioi():
    pages = 'https://vnexpress.net/the-gioi'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='description')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)
@app.route('/vnexpressKinhDoanh', methods=['GET'])
def vnexpressKinhDoanh():
    pages = 'https://vnexpress.net/kinh-doanh'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='description')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)
@app.route('/vnexpressSucKhoe', methods=['GET'])
def vnexpressSucKhoe():
    pages = 'https://vnexpress.net/suc-khoe'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='description')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)
@app.route('/vnexpressGiaoDuc', methods=['GET'])
def vnexpressGiaoDuc():
    pages = 'https://vnexpress.net/giao-duc'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='description')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)
@app.route('/vnexpressPhapLuat', methods=['GET'])
def vnexpressPhapLuat():
    pages = 'https://vnexpress.net/phap-luat'
    page = requests.get(pages)
    web_page = page.content
    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.findAll(class_='description')
    links = [link.find('a').attrs["href"] for link in test]
    return jsonify(links)
def log(message):  # simple wrapper for logging to stdout on heroku
    print(message)
    sys.stdout.flush()

