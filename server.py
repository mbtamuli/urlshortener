from uuid import uuid4
import json, random, string
from flask import Flask, escape, request, redirect, render_template

app = Flask(__name__)

def randomString():
    shortstring=''
    for i in range(8):
        shortstring = shortstring + random.choice(string.ascii_letters+string.digits)
    return shortstring

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        urls = []
        with open('urls.json') as f:
            urls = json.load(f)
        shortURL = randomString()
        urls.update(dict([(shortURL,request.form['url'])]))
        with open('urls.json', 'w') as f:
            json.dump(urls, f)
        return shortURL
    else:
        return render_template('index.html')

@app.route('/id/<shortid>')
def redirectURL(shortid):
    urls = []
    with open('urls.json') as f:
        urls = json.load(f)
    return redirect(urls[shortid])