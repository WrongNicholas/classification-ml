import pandas as pd

df = pd.read_csv("tse_dataset.csv")
df = df[df["category"].isin(["BUG", "FEATURE"])]

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

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(x_train, y_train)

from google_play_scraper import reviews

result, _ = reviews( 
    'us.zoom.videomeetings',
    lang='en', 
    country='us', 
    count=200 
)

texts = [r["content"] for r in result]

predictions = model.predict(vectorizer.transform(texts))

scraped_df = pd.DataFrame({
    "review": texts,
    "predicted_category": predictions
})

scraped_df.to_excel("classified.xlsx", index=False)
print("\n====================================")
print("SAVED TO classified.xlsx:")
print("====================================")
print(scraped_df.head())
