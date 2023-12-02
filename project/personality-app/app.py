from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

app = Flask(__name__)

# Load the personality dataset and train the classifiers
data = pd.read_csv("personality_dataset.csv")
features = data[["openness", "neuroticism","conscientiousness","agreeableness", "extraversion"]]
labels = data["Personality (Class label)"]
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

classifiers = {
    "Gaussian Naive Bayes": GaussianNB(),
    "K-Nearest Neighbors (KNN)": KNeighborsClassifier(n_neighbors=5),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "Support Vector Machines (SVM)": SVC(),
    "Quadratic Discriminant Analysis (QDA)": QuadraticDiscriminantAnalysis()
}

for classifier_name, classifier in classifiers.items():
    classifier.fit(X_train, y_train)

def predict_temperament(user_input):
    # Predict temperament using the trained classifiers
    individual_predictions = []
    for classifier_name, classifier in classifiers.items():
        prediction = classifier.predict([user_input])[0]
        individual_predictions.append((classifier_name, prediction))

    # Calculate the most common prediction
    prediction_counts = {}
    for prediction in individual_predictions:
        prediction_type = prediction[1]
        if prediction_type not in prediction_counts:
            prediction_counts[prediction_type] = 0
        prediction_counts[prediction_type] += 1

    most_common_prediction = max(prediction_counts, key=prediction_counts.get)

    # Calculate the accuracy of each classifier
    accuracy_scores = {}
    for classifier_name, classifier in classifiers.items():
        classifier.fit(X_train, y_train)
        accuracy = classifier.score(X_test, y_test)
        accuracy_scores[classifier_name] = accuracy

    # Return the most common prediction and accuracy scores
    return most_common_prediction, accuracy_scores

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect user input from the HTML form
        user_input = []
        for trait in ["openness", "neuroticism","conscientiousness","agreeableness", "extraversion"]:
            user_input_trait = int(request.form.get(trait, 0))
            user_input.append(user_input_trait)

        # Predict temperament and accuracy scores
        most_common_prediction, accuracy_scores = predict_temperament(user_input)

        # Prepare the result message
        result_message = f"Predicted Temperament (Mode): {most_common_prediction}"
        accuracy_message = f"Accuracy Scores: {accuracy_scores}"

        # Pass the prediction and accuracy data to the HTML template
        return render_template('index.html', result_message=result_message, accuracy_message=accuracy_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
