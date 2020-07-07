import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer


category_dict = {0:'sport',1:'business',2:'tech', \
        3:'entertainment',4:'politics'}

## Recovering vectorizer and model
vectorizer_path = '../src/model/tfidf.pb'
model_path = '../src/model/logistic_model.pb'

with open(vectorizer_path,'rb') as fid:
    tfidf = pickle.load(fid)

with open(model_path,'rb') as feed:
    model = pickle.load(feed)

## Testing 
test_string = """German World Cup Winner Berthold On David Alaba: “Don’t Know Of Inter’s Interest But Seems Man City Are Keen”.Former Roma and Hellas Verona defender Thomas Berthold discussed new Inter right back Achraf Hakimi and the Nerazzurri’s interest in Bayern Munich left back David Alaba in an interview on the TV show ‘Taca La Marca’, hosted by Italian broadcaster Radio Musica Television earlier today.“He’s a great addition to Inter, he’s a very fast player with important physical skills. In the world cup and in international competitions I have seen few really good players in this role, both left and right, so the Nerazzurri have made a great signing.”  """

vectorized_question = tfidf.transform([test_string])
category_pred = model.predict(vectorized_question)
category_str = category_dict.get(category_pred[0])
print("test string predicted category = {}".format(category_str))
