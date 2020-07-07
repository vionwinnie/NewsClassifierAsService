import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


## Training Model
df = pd.read_csv('../src/bbc-text.csv')
df.head()

from collections import Counter
Counter(df.category)
df['category'] = df.category.map({'sport':0,'business':1,'tech':2,'entertainment':3,'politics':4})

## Set random seed
seed = 42
np.random.seed(seed)

## Shuffle Data
def shuffle(df, n=3, axis=0):
    df = df.copy()
    random_states = [2,42,4]
    for i in range(n):
        df = df.sample(frac=1,random_state=random_states[i])
    return df

new_df = shuffle(df)


## Splitting Training and Testing Data
split_idx = int(len(df)*0.8)
print(split_idx)
train_df = new_df.loc[:split_idx,:]
test_df = new_df.loc[split_idx:,:]
print(train_df.groupby(['category'])['text'].count())
print(test_df.groupby(['category'])['text'].count())

## Tfidf Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(train_df.text).toarray()
labels = train_df.category

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

entries = []
CV = 3   # 3-fold validation
model = LogisticRegression()
model_name = 'Logistcic_Regression'
accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
for fold_idx, accuracy in enumerate(accuracies):
    entries.append((model_name, fold_idx, accuracy))

cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
cv_df.groupby('model_name').accuracy.mean()

## Model Performance
X_test = tfidf.transform(test_df.text)
y_test = test_df.category
model.fit(features,labels)
y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_test, y_pred)
print(conf_mat)

from sklearn.metrics import accuracy_score
print("Accuracy: {:.2f}".format(accuracy_score(y_test,y_pred)))

## Export Vectorizer and Logistic Model
import pickle
import os

export_folder = '../src/model'
if not os.path.exists(export_folder):
    os.makedirs(export_folder)

# Export vecotirzer
vectorizer_fname = 'tfidf.pb'
vectorizer_path = os.path.join(export_folder,vectorizer_fname)
with open(vectorizer_path,'wb') as fid:
    pickle.dump(tfidf,fid)

# Export model
model_fname = 'logistic_model.pb'
model_path = os.path.join(export_folder,model_fname)


with open(model_path,"wb") as feed:
    pickle.dump(model,feed)

print('Model Training and Export completed')
