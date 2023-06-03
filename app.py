from flask import Flask, request
from utils import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hi here, this is the project for Public Opinion Analyse Built by BJTU-CIT.'


@app.route('/sentiment_ana')
def sentiment_ana():
    text = request.args.get("text")
    label, labels = predict(text)
    return label


if __name__ == '__main__':
    # TODO：记录日志：logger
    app.run(host='0.0.0.0', port=8888, debug=True)
