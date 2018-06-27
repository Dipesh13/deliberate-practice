from nltk import word_tokenize
from nltk.corpus import stopwords

def preprocess(text):
    """
    lower + remove punctuations,digits and stopwords
    :param text:
    :return:
    """
    text = text.lower()
    doc = word_tokenize(text)
    doc = [word for word in doc if word not in stopwords]
    doc = [word for word in doc if word.isalpha()]
    return doc

# sample call
test = preprocess("Hi i want to buy 5 pizzas from the nearest shop.")
print(test)