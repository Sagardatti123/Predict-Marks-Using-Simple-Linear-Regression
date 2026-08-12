from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# ---------------------------------------------------------
# Load the trained Linear Regression model (marks.pkl)
# ---------------------------------------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "marks.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    hours = ""
    error = None

    if request.method == "POST":
        hours_raw = request.form.get("hours", "").strip()
        try:
            hours = float(hours_raw)

            if hours < 0:
                error = "Study hours cannot be negative."
            elif hours > 24:
                error = "Study hours cannot exceed 24 in a day."
            else:
                # Model expects a 2D array: [[hours]]
                pred_value = model.predict(np.array([[hours]]))[0]
                # pred_value may be a 1-element array depending on how it was fit
                pred_value = float(np.ravel(pred_value)[0])

                # Clamp displayed marks to a realistic 0-100 range
                pred_value = max(0, min(100, pred_value))
                prediction = round(pred_value, 2)

        except ValueError:
            error = "Please enter a valid number for study hours."

    return render_template(
        "index.html",
        prediction=prediction,
        hours=hours,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
