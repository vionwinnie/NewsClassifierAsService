import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, jsonify, request

## Serving Machine Learning Model

## Start Flask
app = Flask(__name__)
category_dict = {0:'sport',1:'business',2:'tech', \
        3:'entertainment',4:'politics'}

## Recovering vectorizer and model
vectorizer_path = './model/tfidf.pb'
model_path = './model/logistic_model.pb'

with open(vectorizer_path,'rb') as fid:
    tfidf = pickle.load(fid)

with open(model_path,'rb') as feed:
    model = pickle.load(feed)

@app.route("/", methods=['POST'])
def do_prediction():
    json = request.get_json()
    text = json['text']
    #df = loader.json_to_df(json)
    vectorized_question = tfidf.transform([text])
    category_pred = model.predict(vectorized_question)
    category_str = [category_dict.get(category_pred[y]for y in category_pred)]
    return jsonify(category_str)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

