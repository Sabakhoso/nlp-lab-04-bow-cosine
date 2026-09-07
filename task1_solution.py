import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# 1. Define the sample input corpus
corpus = [
    "The product performance is amazing and fast",
    "The service was fast and performance was great",
    "Terrible customer service and bad performance"
]

# 2. Instantiate CountVectorizer with English stop words removed
vectorizer = CountVectorizer(stop_words='english')

# 3. Fit and transform the corpus into a sparse matrix
X = vectorizer.fit_transform(corpus)

# 4. Extract the vocabulary feature names
feature_names = vectorizer.get_feature_names_out()

# 5. Convert the transformed sparse matrix into a Pandas DataFrame
df_bow = pd.DataFrame(X.toarray(), columns=feature_names)

# Display the resulting DataFrame
print(df_bow)