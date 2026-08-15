# Predict-Marks-Using-Simple-Linear-Regression

Deployment Link:https://predict-marks-using-simple-linear-zti5.onrender.com

# 📊 Student Marks Prediction using Simple Linear Regression

<p align="center">
  <b>🤖 Machine Learning • 📈 Simple Linear Regression • 🐍 Python • 🌐 Flask</b>
</p>

<p align="center">
  A beginner-friendly Machine Learning project that predicts a student's marks based on the number of hours studied.
</p>

---

## 🚀 Project Overview

**Student Marks Prediction** is a Machine Learning web application built using **Simple Linear Regression**.

The model learns the relationship between:

* 📚 **Independent Variable (X):** Hours Studied
* 🎯 **Dependent Variable (Y):** Marks

After training, the model can predict the expected marks for a given number of study hours.

The trained model is saved as `marks.pkl` and can be integrated into a Flask application for deployment.

---

## 🧠 Machine Learning Model

This project uses **Simple Linear Regression**.

### Linear Regression Equation

```text
Y = mX + b
```

Where:

* `Y` → Predicted Marks
* `X` → Hours Studied
* `m` → Slope / Coefficient
* `b` → Intercept

The trained model in `marks.pkl` contains approximately:

```text
Coefficient: 9.8307
Intercept:   2.5591
```

So the learned relationship is approximately:

```text
Predicted Marks = 9.8307 × Hours + 2.5591
```

> ⚠️ The exact prediction depends on the input and the dataset used during model training.

---

## ✨ Features

* 📈 Simple Linear Regression model
* 📚 Predict marks from study hours
* 🤖 Trained Scikit-learn model
* 💾 Saved model using Pickle
* 🌐 Flask-ready deployment
* 🚀 Gunicorn configuration included
* 🧑‍💻 Beginner-friendly ML project
* ☁️ Suitable for deployment on platforms supporting Python/Flask

---

## 🛠️ Tech Stack

| Technology      | Purpose              |
| --------------- | -------------------- |
| 🐍 Python       | Programming language |
| 🤖 Scikit-learn | Machine Learning     |
| 📊 Pandas       | Data processing      |
| 🔢 NumPy        | Numerical operations |
| 🌐 Flask        | Web application      |
| 💾 Pickle       | Model serialization  |
| 🚀 Gunicorn     | Production server    |

---

## 📁 Project Structure

```text
Student-Marks-Prediction/
│
├── app.py              # Flask application
├── marks.pkl           # Trained Linear Regression model
├── Procfile            # Deployment configuration
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Web interface
│
└── README.md           # Project documentation
```

---

## 🔄 How It Works

```text
          📚 Hours Studied
                 │
                 ▼
        ┌─────────────────┐
        │  Input Feature  │
        │      Hours      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Linear Regression│
        │      Model      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Predicted Marks │
        └─────────────────┘
```

### Workflow

1. Collect student study-hour data.
2. Separate the independent and dependent variables.
3. Split the dataset into training and testing data.
4. Train the **Linear Regression** model.
5. Evaluate the model.
6. Save the trained model as `marks.pkl`.
7. Load the model inside Flask.
8. Accept study hours from the user.
9. Generate predicted marks.
10. Display the prediction through the web interface.

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/student-marks-prediction.git
cd student-marks-prediction
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

### 3️⃣ Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Then open the local URL displayed by Flask, usually:

```text
http://127.0.0.1:5000/
```

Enter the number of hours studied and get the predicted marks.

---

## 🚀 Deployment

The project includes a `Procfile` configured for Gunicorn:

```text
web:gunicorn :app:app
```

This allows the Flask application to be served using **Gunicorn** on compatible deployment platforms.

> Make sure your actual Flask entry-point filename and Gunicorn syntax match your project before deployment.

---

## 💡 Example

Suppose a student studies:

```text
Hours = 5
```

The trained regression equation gives approximately:

```text
Marks = 9.8307 × 5 + 2.5591
```

```text
Predicted Marks ≈ 51.71
```

This demonstrates how the model uses the learned linear relationship to make predictions.

---

## 🎯 Learning Objectives

This project helped demonstrate the complete basic Machine Learning workflow:

* ✅ Understanding independent and dependent variables
* ✅ Data preprocessing
* ✅ Train-test splitting
* ✅ Simple Linear Regression
* ✅ Model training
* ✅ Prediction
* ✅ Model evaluation
* ✅ Model serialization using Pickle
* ✅ Flask integration
* ✅ ML model deployment

---

## 🔮 Future Improvements

* 📊 Add a visualization of the regression line
* 📈 Display model accuracy metrics
* 🎨 Improve the frontend UI
* 📱 Make the interface responsive
* 🔐 Add input validation
* ☁️ Deploy the application publicly
* 📉 Add more student-related features
* 🤖 Compare Linear Regression with other ML algorithms

---

## ⚠️ Model Compatibility Note

The included `marks.pkl` was created using **Scikit-learn 1.6.1**, while the environment used to inspect it currently has **Scikit-learn 1.8.0**.

For reliable model loading, it is recommended to use the same Scikit-learn version that was used to train and serialize the model, or retrain and save the model using your current environment.

---

## 👨‍💻 Author

**Sagar datti**

🎓 B.Tech — Computer Science & Engineering (Data Science)

💡 Aspiring Data Scientist / Machine Learning Engineer

---

## ⭐ If You Like This Project

If this project helped you understand **Simple Linear Regression and ML deployment**, consider giving the repository a ⭐.

<p align="center">
  <b>Made with 🐍 Python & 🤖 Machine Learning</b>
</p>
