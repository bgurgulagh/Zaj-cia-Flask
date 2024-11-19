from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/kenobi')
def hello_kenobi():
    return 'General Kenobi!'

@app.route('/kenobigen')
def kenobigen():
    return r'<img src="https://i.ytimg.com/vi/qLAQCYSi1_4/maxresdefault.jpg">'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'Użyto metody POST'
    else:
        return 'Użyto metody GET'
    
@app.route('/hello/<name>')
def hello_name(name):
    return f'Witaj, {name}!'

@app.route('/calc/<liczba>')
def calc(liczba):
    return f'{int(liczba)+6}'