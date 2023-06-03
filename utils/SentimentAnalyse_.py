from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

# transformers中所需的离线模型
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
# 下面皆以上述MODEL为依据制作tokenizer、config、model
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)


def preprocess(text):
    """
    预处理：对输入句做简单处理，目前仅针对twitter数据：① 去除url；② 替换所有@ABC未'@USER`
    :param text: 单个输入
    :return: 返回formatted的句子
    """
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


def predict(text=""):
    """
    接收原始输入（单句）
    :param text: 原始输入
    :return: label-预测情感；labels-三类情感及其概率预测
    """
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    label = config.id2label[ranking[0]]
    labels = "(" + config.id2label[ranking[0]] + "," + str(np.round(float(scores[ranking[0]]), 4)) + ");" \
             + "(" + config.id2label[ranking[1]] + "," + str(np.round(float(scores[ranking[1]]), 4)) + ");" \
             + "(" + config.id2label[ranking[2]] + "," + str(np.round(float(scores[ranking[2]]), 4)) + ")"
    return label, labels


if __name__ == '__main__':
    print(predict("i'm very hungry now"))
