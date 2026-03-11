import pandas as pd

df = pd.read_csv("tse_dataset.csv")

# print(df.head())

x = df["body"]
y = df["category"]

print(df["category"].value_counts())
print("\n")

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english")

x = vectorizer.fit_transform(x)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42,
    stratify=y # preserve class proportions in train/test
)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

predictions = model.predict(x_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions, average="weighted", zero_division=0))
print("Recall:", recall_score(y_test, predictions, average="weighted", zero_division=0))
print("F1 Score:", f1_score(y_test, predictions, average="weighted", zero_division=0))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
