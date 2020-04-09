import datetime
from flask import Flask, request
from time import localtime, time

app = Flask(__name__)

messages=[
    {'username': 'Nick', 'text': 'Hello', 'time': 0.0}
]

@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/status")
def status():

    return {
        'status': True,
        'name': 'Ogrgram',
        'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


@app.route("/send", methods=['POST'])
def send():
    username = request.json['username']
    text = request.json['text']
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    messages.append(message)

    print(messages)

    return {"ok": True}

app.run()