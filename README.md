# 🏥 Health AI – Smart Healthcare System

A full-stack **Health AI – Smart Healthcare System** developed using **Python, Flask, and Scikit-learn** to predict likely diseases from user-selected symptoms and generate a complete health report covering descriptions, precautions, medications, diet plans, and workout suggestions.

> ⚠️ **Disclaimer:** This project is for educational purposes only. It is **not** a medical diagnosis tool. Always consult a qualified healthcare professional.

---

# 📸 Application Preview

![Home Page](https://github.com/user-attachments/assets/91da35de-645f-4efe-add8-76a14a3ff83d)

---

# 🎯 Project Objective

The objective of this project is to build a web application that lets users select their symptoms and instantly receive a machine-learning-based disease prediction along with practical health guidance. It combines a trained classification model with several supporting datasets to turn raw symptom input into a readable health report.

The application helps users understand:
* Most Likely Disease
* Prediction Confidence Score
* Plain-Language Disease Description
* Recommended Precautions
* Common Medications
* Diet Plan
* Workout Suggestions

---

# 💼 Business Problem

People who feel unwell often search symptoms across many websites and get scattered, confusing, or alarming information. There is no single place that links a set of symptoms to a likely condition and the next practical steps.

This system transforms symptom input into a structured health report, giving users an easy-to-read starting point for understanding their condition before consulting a doctor.

---

# ❓ Key Analytical Questions

* Which disease is most likely given a specific combination of symptoms?
* How confident is the model in its prediction?
* What precautions are recommended for the predicted disease?
* Which medications, diet, and workouts are commonly associated with it?
* Is the user input valid and complete before a prediction is made?

---

# 🛠️ Tools & Technologies

* **Front-End:** HTML, CSS, JavaScript, Bootstrap 5, Jinja2 templates
* **Back-End:** Python 3, Flask (application factory + blueprints)
* **Machine Learning:** Scikit-learn (Support Vector Classifier, RBF kernel)
* **Data Manipulation:** Pandas, NumPy
* **Model Persistence:** Joblib
* **Configuration & Logging:** python-dotenv, Python logging

---

# 📂 Dataset / Schema

The project uses a symptom-disease dataset and five supporting CSV files that are merged for each predicted disease.

**Training Data (`Training.csv`):**
* 132 symptom columns (binary: 1 = present, 0 = absent)
* `prognosis` column (disease name, 41 classes)

**Supporting Data:**

| File | Purpose |
| ---- | :--- |
| `description.csv` | Plain-language disease description |
| `precautions_df.csv` | Four recommended precautions per disease |
| `medications.csv` | Common medications per disease |
| `diets.csv` | Recommended diet plan |
| `workout_df.csv` | Workout suggestions |
| `symtoms_df.csv` | Symptom reference details |

**Data cleaning:** empty columns and duplicate rows are removed before training.

---

# 📈 Key Report Metrics

| Metric | Description |
| ---------------------- | :--- |
| **Predicted Disease** | Disease with the highest model probability |
| **Confidence Score** | Probability assigned to the prediction |
| **Description** | Short explanation of the disease |
| **Precautions** | Four recommended precautions |
| **Medications** | Common medicines associated with the disease |
| **Diet & Workout** | Suggested diet plan and workouts |

---

# 📊 Application Features

### 1. Interactive Symptom Selector
Search and click-to-select chip interface covering 132 symptoms, with a live counter of selected symptoms.

![Symptom Selector](https://github.com/user-attachments/assets/db78dc8a-c9c7-4b0f-8df9-06f11c7c6f9f)

### 2. Machine Learning Prediction
A Support Vector Classifier trained on 41 diseases returns the most likely disease with a confidence score. Input is validated before it reaches the model.

### 3. Complete Health Report
Merges five supporting datasets with Pandas to build a full report for the predicted disease, with a print-friendly layout.

![Health Report](https://github.com/user-attachments/assets/3cf0feb2-615c-4a56-b4f6-a15663c0037a)

### 4. Health Blog & Informational Pages
Includes a health blog (list and detail pages), About, Developer, and Contact pages.

### 5. Clean, Modular Architecture
Built with the Flask application factory pattern, separate blueprints for main pages, prediction, and blog, plus dedicated utilities for validation, prediction logic, and logging.

---

# 🧠 Model Training

| Step | Details |
| ---- | :--- |
| Split | Stratified train-test split |
| Model | SVC with RBF kernel |
| Validation | Cross-validation scores printed during training |
| Output | `svc_model.pkl` and `label_encoder.pkl` |

> **Note:** The dataset is small and highly repetitive, so scores are near-perfect. They reflect the dataset and do not indicate real-world clinical accuracy.

To retrain the model:

```bash
python models/model_trainer.py
```

---

# 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/sainathapar007/Smart-Healthcare-System.git
cd Smart-Healthcare-System

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env         # then set a strong SECRET_KEY

# 5. Run the app
python app.py
```

Open **http://localhost:5000** in your browser.

| Page | Route |
| ---- | :--- |
| Home | `/` or `/home` |
| Check Symptoms | `/predict/` |
| Health Blog | `/blog/` |
| About | `/about` |
| Developer | `/developer` |
| Contact | `/contact` |

---

# ⚠️ Limitations

* Predictions use symptom presence only (no age, medical history, or test results).
* Medication and diet details are general reference data, not personalized advice.
* Predictions are not stored (no database in this version).

---

# 🔮 Future Improvements

* Show the top 3 predictions with probabilities
* Add user accounts and prediction history with a database
* Add model evaluation charts (confusion matrix)
* Deploy online (Render / Hugging Face Spaces)

---

# 📁 Project Files

```text
Smart-Healthcare-System/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── routes/
│   ├── main_routes.py
│   ├── prediction_routes.py
│   └── blog_routes.py
│
├── utils/
│   ├── prediction_service.py
│   ├── validators.py
│   └── logger.py
│
├── models/
│   ├── model_trainer.py
│   ├── svc_model.pkl
│   └── label_encoder.pkl
│
├── data/
│   ├── Training.csv
│   ├── description.csv
│   ├── precautions_df.csv
│   ├── medications.csv
│   ├── diets.csv
│   ├── workout_df.csv
│   └── symtoms_df.csv
│
├── templates/
└── static/
```

---

# 👨‍💻 Author

**Sainath Apar**
B.Tech – Computer Science & Engineering

* LinkedIn: [linkedin.com/in/sainathapar](https://www.linkedin.com/in/sainathapar)
* GitHub: [github.com/sainathapar007](https://github.com/sainathapar007)
