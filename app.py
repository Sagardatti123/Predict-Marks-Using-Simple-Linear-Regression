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

COEF = float(np.ravel(model.coef_)[0])
INTERCEPT = float(np.ravel(model.intercept_)[0])

# The hours value at which the raw (unclamped) line crosses 100 marks.
# Beyond this point the model is extrapolating past what a 0-100 mark
# scale can represent, so predictions there are shown as "unreliable".
SAFE_HOURS = (100 - INTERCEPT) / COEF if COEF != 0 else 0

# Chart geometry (SVG viewBox units) used to draw the regression line
# and the plotted point on the frontend.
CHART_W = 560
CHART_H = 300
X_DOMAIN = 24     # hours axis: 0-24
Y_DOMAIN = 100     # marks axis: 0-100


def to_px_x(hours):
    return round((hours / X_DOMAIN) * CHART_W, 1)


def to_px_y(marks):
    # inverted: 0 marks -> bottom (CHART_H), 100 marks -> top (0)
    return round(CHART_H - (marks / Y_DOMAIN) * CHART_H, 1)


def line_segment(x1_hours, x2_hours):
    y1 = COEF * x1_hours + INTERCEPT
    y2 = COEF * x2_hours + INTERCEPT
    return {
        "x1": to_px_x(x1_hours), "y1": to_px_y(y1),
        "x2": to_px_x(x2_hours), "y2": to_px_y(y2),
    }


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    raw_prediction = None
    reliable = True
    hours = ""
    error = None
    point = None

    if request.method == "POST":
        hours_raw = request.form.get("hours", "").strip()
        try:
            hours = float(hours_raw)

            if hours < 0:
                error = "Study hours cannot be negative."
            elif hours > 24:
                error = "Study hours cannot exceed 24 in a day."
            else:
                raw_value = float(np.ravel(model.predict(np.array([[hours]])))[0])
                raw_prediction = round(raw_value, 2)

                reliable = 0 <= raw_value <= 100
                prediction = round(max(0, min(100, raw_value)), 2)

                point = {"x": to_px_x(hours), "y": to_px_y(max(0, min(100, raw_value)))}

        except ValueError:
            error = "Please enter a valid number for study hours."

    # Regression line split at SAFE_HOURS: solid where the model is
    # within the 0-100 mark range, dashed where it's extrapolating.
    solid_end = min(max(SAFE_HOURS, 0), X_DOMAIN)
    solid_segment = line_segment(0, solid_end)
    dashed_segment = line_segment(solid_end, X_DOMAIN) if solid_end < X_DOMAIN else None

    chart = {
        "w": CHART_W,
        "h": CHART_H,
        "solid": solid_segment,
        "dashed": dashed_segment,
        "safe_hours_x": to_px_x(solid_end),
        "safe_hours_label": round(solid_end, 1),
    }

    tech_stack = [
        "Python",
        "Flask",
        "scikit-learn (Linear Regression)",
        "NumPy",
        "Pickle",
        "Jinja2",
        "HTML5 & CSS3",
    ]

    return render_template(
        "index.html",
        prediction=prediction,
        raw_prediction=raw_prediction,
        reliable=reliable,
        hours=hours,
        error=error,
        point=point,
        chart=chart,
        tech_stack=tech_stack,
        coef=round(COEF, 3),
        intercept=round(INTERCEPT, 3),
        author="Sagar Datti",
    )


if __name__ == "__main__":
    app.run(debug=True)