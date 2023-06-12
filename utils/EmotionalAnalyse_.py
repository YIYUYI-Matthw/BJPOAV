'''
1. 从https://huggingface.co/cardiffnlp/twitter-roberta-base-emotion-multilabel-latest下载模型权重放到本地文件夹下
2. 假设路径为/emotional_analysis
3. 此文件第23行的model路径改为本地路径
3. 安装依赖包
    pip install tweetnlp
    pip install -U tensorflow==2.10
'''
from transformers import pipeline
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
# 遍历情绪列表，找到最大概率对应的情绪标签
def clean_result(result):
    max_score = 0.0
    max_label = ''
    for emotion in result[0]:
        if emotion['score'] > max_score:
            max_score = emotion['score']
            max_label = emotion['label']
    return max_label
def predict_emotion(x):
    pipe = pipeline("text-classification", model=r"D:\jupyter_code\中国故事\emotionalanalysis-tweetnlp\emotional_analysis",return_all_scores=True)
    return pipe(preprocess(x)),clean_result(pipe(preprocess(x)))
if __name__=="__main__":
    '''
        返回结果为：共11种情绪
        [[{'label': 'anger', 'score': 0.3670094311237335}, 
        {'label': 'anticipation', 'score': 0.033516861498355865}, 
        {'label': 'disgust', 'score': 0.5650255084037781}, 
        {'label': 'fear', 'score': 0.27044370770454407}, 
        {'label': 'joy', 'score': 0.00960608571767807}, 
        {'label': 'love', 'score': 0.005090760532766581}, 
        {'label': 'optimism', 'score': 0.008916712366044521}, 
        {'label': 'pessimism', 'score': 0.5608734488487244}, 
        {'label': 'sadness', 'score': 0.9554517865180969}, 
        {'label': 'surprise', 'score': 0.01900850608944893}, 
        {'label': 'trust', 'score': 0.0055234236642718315}]]
    '''
    print(predict_emotion("i'm very hungry now")[1])
    

