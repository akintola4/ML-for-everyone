import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('rhetorical_questions.csv')

# Separate features and labels
X = data['question']
y = data['label']

# Vectorize the text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)

# Train the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model performance
accuracy = classifier.score(X_test, y_test)
print('Accuracy:', accuracy)

# Define a function to predict whether a question is rhetorical or not
def is_rhetorical(question):
   
     # Convert the question to a vector
    question_vec = vectorizer.transform([question])

    # Predict the label
    label = classifier.predict(question_vec)

    # Return the prediction
    if label[0] == 1:
        return True
    else:
        return False

# Example usage
question = "Is the sky blue?"
if is_rhetorical(question):
    print(question, "is a rhetorical question.")
else:
	print(question, "is not a rhetorical question.")