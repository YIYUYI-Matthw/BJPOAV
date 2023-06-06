# TODO：聚类
# Data processing
import nltk

# nltk.download('stopwords')  # VPN
# Dimension reduction
from umap import UMAP
# Count vectorization
from sklearn.feature_extraction.text import CountVectorizer
# Topic model
from bertopic import BERTopic

# NLTK English stopwords
stopwords = nltk.corpus.stopwords.words('english')

# Initiate UMAP
umap_model = UMAP(n_neighbors=15,
                  n_components=5,
                  min_dist=0.0,
                  metric='cosine',
                  random_state=100)
# Count vectorizer
vectorizer_model = CountVectorizer(stop_words=stopwords)

topic_30 = BERTopic(umap_model=umap_model,
                    vectorizer_model=vectorizer_model,
                    min_topic_size=100,  # cluster至少包含多少样本
                    top_n_words=5,
                    language="english",
                    calculate_probabilities=True)


def cluster(comments):
    if len(comments) < 100:
        print(f"more samples needed ({len(comments)} is provided for now.")
        return None
    topic_30.fit_transform(comments)
    return topic_30


if __name__ == '__main__':
    comments = [
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER Evil Chinaxis and Xitler perpetr cultural genocide against the Uyghur woman and people in East Turkestan",
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER This be just to assert that Germany consid itself a a watchdog of democracy Germany never dare to speak a word against China 's repression of Uyghur Muslims This could also be in retaliation to a snub by USER recently while ask them to mind their own business"
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "USER USER USER No I refer to Chechen war and Uyghur genocide",
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
        "While Dan Andrews visit China to discu trade spare a think for young Melbourne nurse USER Her Uyghur husband wa sentence to 25 year in prison by the CCP solely because of the colour of his skin and she miss him every day There be more to life than trade"
    ]
    print("clustering...")
    topics = cluster(comments)
    print(topics.get_topic_info())
    print(topics.get_document_info(comments))