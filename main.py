import pandas as pd

df = pd.read_csv("tse_dataset.csv")
df = df[df["category"].isin(["BUG", "FEATURE"])]

# print(df.head())

x = df["body"]
y = df["category"]

print(df["category"].value_counts())
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC

models = {
    "DECISION_TREE": DecisionTreeClassifier(),
    "RANDOM_FOREST": RandomForestClassifier(),
    "SVM": LinearSVC()
}

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

for name, model in models.items():
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    print("\n====================================")
    print(name)
    print("====================================")

    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Precision:", precision_score(y_test, predictions, average="weighted", zero_division=0))
    print("Recall:", recall_score(y_test, predictions, average="weighted", zero_division=0))
    print("F1 Score:", f1_score(y_test, predictions, average="weighted", zero_division=0))


    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

