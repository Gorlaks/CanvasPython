import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from canvas.models.canvas import CanvasDataToSend


stopwords = ["a", "the"]
vectorizer = TfidfVectorizer()
Spam_model = LogisticRegression(solver='liblinear', penalty='l1')


def study():
    data = pd.read_csv("spam.csv", encoding="latin-1")

    messages = data["v2"]

    message_types = data["v1"]

    processed_messages = remove_stopwords(messages)

    vectorized_X = vectorizer.fit_transform(processed_messages)

    message_train, message_test, message_types_train, message_types_test = train_test_split(vectorized_X, message_types, test_size=0.3, random_state=20) 

    Spam_model.fit(message_train, message_types_train)


def check_data_for_spam(data: CanvasDataToSend):
    total_cells = len(data.data)
    total_spam = 0
    for item in data.data:
        content = item['content']
        if (len(content) == 0):
            return 'Fill all fields'
            break
        res = find_spam(content)
        if (res == 'spam'):
            total_spam += 1
        
    if (total_spam < total_cells / 2):
        return False
    else:
        return True


def find_spam(text):
    dataForPredict = remove_stopwords(pd.DataFrame(data={
        "v2": [text]
    })["v2"])

    X_val = vectorizer.transform(dataForPredict)

    result = Spam_model.predict(X_val)[0]
    return result


def remove_stopwords(messages):
    processed_messages = []
    for sentence in messages:
        list = [word for word in sentence.split(
            " ") if (word not in stopwords)]
        processed_sentence = " ".join(list)
        processed_messages.append(processed_sentence)
    return processed_messages