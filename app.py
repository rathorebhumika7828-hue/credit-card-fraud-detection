from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("models/fraud_detection_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    probability = None

    if request.method == "POST":

        # Get all 30 features from form
        features = [
            "Time",
            "V1", "V2", "V3", "V4", "V5", "V6", "V7",
            "V8", "V9", "V10", "V11", "V12", "V13", "V14",
            "V15", "V16", "V17", "V18", "V19", "V20", "V21",
            "V22", "V23", "V24", "V25", "V26", "V27", "V28",
            "Amount"
        ]

        values = []

        for feature in features:
            value = float(request.form[feature])
            values.append(value)

        # Convert input into DataFrame
        input_data = pd.DataFrame([values], columns=features)

        # Prediction
        prediction = model.predict(input_data)[0]

        # Fraud probability
        probability = model.predict_proba(input_data)[0][1] * 100

        if prediction == 1:
            result = "⚠️ FRAUD TRANSACTION"
        else:
            result = "✅ NORMAL TRANSACTION"

    return render_template(
        "index.html",
        result=result,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=True)