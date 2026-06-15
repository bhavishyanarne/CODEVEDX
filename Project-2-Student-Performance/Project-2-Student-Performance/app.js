import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("dataset.csv")

X = data[["attendance","marks","study_hours"]]
y = data["performance"]

model = LogisticRegression()
model.fit(X,y)

attendance = int(input("Attendance: "))
marks = int(input("Marks: "))
hours = int(input("Study Hours: "))

result = model.predict([[attendance,marks,hours]])

if result[0] == 1:
    print("Good Performance")
else:
    print("Poor Performance")
