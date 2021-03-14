from flask import Flask, jsonify, request, Response, render_template
from pykafka import KafkaClient
import json


def get_kafka_client():
    return KafkaClient(hosts='localhost:9092')


app = Flask(__name__)

# main page here
# /home이라고 하면 주소에서 local:5001/home 이런식으로 들어가야대
@app.route("/")
def index():
    #return (render_template('index.html'))
    return('LEAFLET MAP')

# consumer로 받은것들을 보여주는거
# localhost:5001/topic/twitterdataa2로 들어가야 보일 수 있어어@app.route('/topic/<topicname>')
@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()

    def events():
        for i in client.topics[topicname].get_simple_consumer():
            # byte로 나오기에 decode
            yield 'data:{0}\n\n'.format(i.value.decode())

    return (Response(events(), mimetype="text/event-stream"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)