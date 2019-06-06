import markovify
import json
from flask import Flask, render_template
aneks = json.load(open('aneks.json'))

text = ""

for anek in aneks:
    text += anek['text']

m = markovify.Text(text)

app = Flask(__name__)

@app.route('/')
def index():
    L = []
    for i in range(5):
        L.append(m.make_sentence().replace('\r\n', '<br>').replace('\n', '<br>'))
    text = '<p>' + '</p><p>'.join(L) + '</p>'
    return render_template('index.html', text=text)

app.run(port='9095')

