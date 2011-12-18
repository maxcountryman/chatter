from chatter import app
from flask import request, render_template, jsonify
from juggernaut import Juggernaut

jug = Juggernaut()

chat_buffer = []
user_counter = [0]


@app.route('/')
def index():
    return render_template('index.html', chat_buffer=chat_buffer)


@app.route('/_chat', methods=['POST'])
def _chat():
    user = request.form.get('user_id')
    message = request.form.get('message')
    message = user + ': ' + message
    chat_buffer.append(message)
    jug.publish('chat', message)
    return jsonify(result='OK')


@app.route('/_on_connect', methods=['POST'])
def on_connect():
    user_id = user_counter[0]
    user_counter[0] += 1
    return jsonify(user_id='user' + str(user_id))


@app.route('/_on_disconnect', methods=['POST'])
def on_disconnect():
    counter = user_counter[0]
    if counter > 0:
        counter -= 1
    return jsonify(result='OK')


if __name__ == '__main__':
    app.run()
