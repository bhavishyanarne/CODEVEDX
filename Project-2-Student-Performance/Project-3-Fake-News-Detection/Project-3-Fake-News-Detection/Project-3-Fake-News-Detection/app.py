import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("news.csv")

X = data["text"]
y = data["label"]

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

news = input("Enter News: ")

test = vectorizer.transform([news])

prediction = model.predict(test)

print("Prediction:", prediction[0])
