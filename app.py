import time
import queue

from flask import Flask, Response, request

app = Flask(__name__)

queues = {}


def stream(name):
    queues[name] = stream_queue = queue.Queue()

    while True:
        try:
            yield f'{stream_queue.get()}\n'
        except GeneratorExit:
            break

    del queues[name]


@app.route('/<name>')
def index(name):
    return Response(stream(name), mimetype='text/event-stream')


@app.route('/give', methods=('GET', 'POST'))
def give():
    if request.method == 'POST' and request.form['name'] in queues:
        queues[request.form['name']].put(request.form['points'])

    return (
        '<form method="post">'
        '   Name to give to: <input name="vcvcvcvcvcv"><br>'
        '   Points to give: <input name="points"><br>'
        '   <input type="submit">'
        '</form>'
    )