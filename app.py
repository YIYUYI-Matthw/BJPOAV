from utils import *
from flask import Flask, render_template, jsonify, make_response, request
import os
import base64

app = Flask(__name__)


@app.route('/get_image_list', methods=['GET'])
def get_image_list():
    image_folder = './static/image'  # 图片文件夹的路径
    image_list = []
    for filename in os.listdir(image_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_list.append(filename)
    return jsonify({'image_list': image_list})


@app.route('/get_base64_image', methods=['POST'])
def get_base64_image():
    image_name = request.json['image_name']  # 假设前端传递了图片名称
    image_path = os.path.join('./static/image', image_name)  # 图片的完整路径
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return jsonify({'base64_data': encoded_string})


@app.route('/wordcloud')
def draw_wordcloud():
    return render_template('index.html')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hi here, this is the project for Public Opinion Analyse Built by BJTU-CIT.'


@app.route('/sentiment_ana')
def sentiment_ana():
    text = request.args.get("text")
    label, labels = predict(text)
    return label


@app.route("/world_map")
def world_map():
    # TODO：把后续的巴拉巴拉做好
    pass


if __name__ == '__main__':
    # TODO：记录日志：logger
    app.run(host='0.0.0.0', port=8888, debug=True)
